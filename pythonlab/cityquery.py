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

test_connection()

# This function sends an SQL query to the database
def test_query_one():

	conn = psycopg2.connect(
	    host="localhost",
	    port=5432,
	    database="yangl4",
	    user="yangl4",
	    password="stars929bond")
	
	cur = conn.cursor()

	sql1 = """SELECT city, lat, lon FROM cities WHERE city = 'Northfield';"""
    
	cur.execute( sql1 )

    # fetchall() returns a list containing all rows that matches your query    
	row_list = cur.fetchall()
	
	for row in row_list:
		if row[1] == "Northfield":
			print("Northfield's latitude is {} and longitude is {}.".format( row[2], row[3])) 
			break
	print("Northfield is not in the database.")

	conn.commit()
	conn.close()

	return None

test_connection()
test_query_one()
