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
def execute_queries():

	conn = psycopg2.connect(
	    host="localhost",
	    port=5432,
	    database="yangl4",
	    user="yangl4",
	    password="stars929bond")
	
	cur = conn.cursor()

	# Query 1 determines if Northfield is present in the database, then prints its location if it does. 
	sql1 = """SELECT city, lat, lon FROM cities WHERE city = 'Northfield';"""
	cur.execute( sql1 )

	row_list = cur.fetchall()
	for row in row_list:
		if row[0] == "Northfield":
			print("Northfield's latitude is {} and longitude is {}.".format( row[1], row[2] )) 
			break
	print("Northfield is not in the database.")

	# Query 2 prints name of the city with the largest population
	sql2 = """SELECT city, pop FROM cities ORDER BY pop DESC;"""
	cur.execute( sql2 )

	print("{} is the city with the largest population.".format( cur.fetchone()[0] ))

	# Query 3 prints name of the city in MN with the smallest population
	sql3 = """SELECT city, state, pop FROM cities WHERE state = 'Minnesota' ORDER BY pop;"""
	cur.execute( sql3 )

	print("{} is the city with the smallest population in Minnesota.".format( cur.fetchone()[0] ))

	# Query 4 prints names of the cities that is furthest North, East, South, or West
	sql4 = """SELECT city, lat, lon FROM cities ORDER BY {};"""

	north = 'lat DESC'
	east = 'lon DESC'
	south = 'lat'
	west = 'lon'

	cur.execute( sql4.format(north) )
	print("{} is the city that is furthest North.".format( cur.fetchone()[0] ))

	cur.execute( sql4.format(east) )
	print("{} is the city that is furthest East.".format( cur.fetchone()[0] ))

	cur.execute( sql4.format(south) )
	print("{} is the city that is furthest South.".format( cur.fetchone()[0] ))

	cur.execute( sql4.format(west) )
	print("{} is the city that is furthest West.".format( cur.fetchone()[0] ))

	# Query 5 gets State name as input and prints the total population of all cities in the state.
	state  = input("Enter the name of state, full or abbreviation: ").upper()
	total_pop = 0

	if len(state) == 2:
		sql5 = """SELECT state, abb FROM states WHERE abb.upper = %s;"""
		cur.execute( sql5, [state.upper()] )
		state = cur.fetchone()[0]

	sql5 = """SELECT state, pop FROM cities WHERE state.upper() = %s;"""
	cur.execute( sql5, [state])

	row_list = cur.fetchall()
	for row in row_list:
		total_pop += row[1]
	print("{} is the total population of of all cities in state {}.".format( total_pop, state ))

	conn.commit()
	cur.close()
	conn.close()

	return None

test_connection()
execute_queries()
