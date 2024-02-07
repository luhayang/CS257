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

	sql_table = """DROP TABLE IF EXISTS populations; CREATE TABLE states (code text, state text, pop int);"""

	cur.execute(sql_table)

	conn.commit()
	return None

test_connection()
create_table()
