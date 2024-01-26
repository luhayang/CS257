import psycopg2

def test_connection():
	
conn = psycopg2.connect("yangl4")
cur = conn.cursor()
cur.execute("SELECT * FROM cities")
cur.execute("SELECT * FROM states")
conn.commit()

DROP TABLE IF EXISTS states;
CREATE TABLE states (
  state text,
  abbreviation text
);

DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
  city text,
  state text,
  population int,
  lat double,
  lon double
);
