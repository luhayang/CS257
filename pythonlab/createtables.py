import psycopg2

def test_connection():
	conn = psycopg2.connect(
		host="localhost",
		port=5432,
		database="yangl4",
		user="yangl4",
		password="stars929bond")
	if conn is not None:
		print("Con3nection Worked!")
	else:
		print("Problem with Connection")

	conn.commit()
	return None

# This function creates table
def create_table():
	conn = psycopg2.connect(
		host="localhost",
		port=5432,
		database="yangl4",
		user="yangl4",
		password="stars929bond")
	
	cur = conn.cursor()

	sql_table1 = """DROP TABLE IF EXISTS states; CREATE TABLE states (state text,abb text);"""
	sql_table2 = """DROP TABLE IF EXISTS cities;CREATE TABLE cities (city text,state text,pop int,lat float,lon float);"""

	cur.execute(sql_table1)
	cur.execute(sql_table2)

	conn.commit()
	return None

test_connection()
create_table()
