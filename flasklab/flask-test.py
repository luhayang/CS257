import flask
import psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
	return "Hello World!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
	the_string = "The words are: " + word1 + " and " + word2;
	return the_string

@app.route('/color/<word1>')
def my_color(word1):
	return '<h1 style="color:SlateBlue">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def my_add(num1, num2):
	the_sum = int(num1) + int(num2)
	the_string = "The sum of " + num1 + " and " + num2 + " is " + str(the_sum) + ".";
	return the_string
	
@app.route('/pop/<abbrev>')
def my_pop(abbrev):
	conn = psycopg2.connect(host="localhost", port = 5432, database="yangl4", user="yangl4", password="stars929bond")
	cur = conn.cursor()
	sql = """SELECT * FROM populations WHERE code = %s;"""
	cur.execute(sql, [abbrev])
	row = cur.fetchone()
	the_string = "The population of " + row[1] + " state is " + str(row[2]) + ".";
	
	conn.commit()
	cur.close()
	conn.close()
	
	return the_string

if __name__ == '__main__':
	my_port = 5137
	app.run(host='0.0.0.0', port = my_port)
