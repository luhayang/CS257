import psycopg2

# This function tests to make sure that you can connect to the database
def test_connection():
	
	conn = psycopg2.connect(
		host="localhost",
		port=5432,
		database="yangl4",
		user="yangl4",
		password="stars929bond")
  
	if conn is not None:
		print("Connection Worked!")
	else:
		print("Problem with Connection")

	conn.commit()
	conn.close()
	return None

# This function sends a SQL query to the database
def execute_query():
  
	conn = psycopg2.connect(
		host="localhost",
		port=5432,
		database="yangl4",
		user="yangl4",
		password="stars929bond")

	cur = conn.cursor()

	# This query creates a view that shows top 10 cities that make up the largest proportion in their state population
	create_view = """DROP VIEW IF EXISTS pop_proportion; 
		CREATE VIEW pop_proportion 
		AS SELECT cities.city AS city, populations.code AS code, 
		populations.pop AS state_pop, cities.pop AS city_pop, 
		(CAST(cities.pop AS REAL) / CAST(populations.pop AS REAL)) AS proportion 
		FROM populations JOIN cities ON populations.state = cities.state;"""

	sql = """SELECT * FROM pop_proportion ORDER BY proportion DESC LIMIT 10;"""

	cur.execute(create_view)
	cur.execute(sql)

	row_list = cur.fetchall()

	print("Following cities make up the largest proportion of their state population:")
	for row in row_list:
		print("{}, {} makes up {:.2f}%.".format(row[0], row[1], round(row[4], 2)*100)) 

	conn.commit()
	cur.close()
	conn.close()
	return None

test_connection()
execute_query()
