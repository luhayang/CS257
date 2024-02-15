from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/rand/<low>/<high>')
def rand(low, high):
    #Input values that come from a URL (i.e., @app.route)
    #   are always strings so I need to convert the type to int
    low_int = int(low)
    high_int = int(high)
    
    num = random.randint(low_int, high_int)
    return render_template("random.html", randNum = num)



names = ['Alice', 'Alberto', 'Adeline', 'Chance', 'Tariq', 'Enrique', 'Karlie', 'Tatyana', 'Nicole', 'Elaine', 'Raul', 'Khalid', 'Annemarie']
adjectives = ['Aggressive', 'Rebel', 'Elite', 'Various', 'Keen', 'Hypnotic', 'Sable', 'Marked', 'Known', 'Scarce', 'Average', 'Wise', 'Brave']

@app.route('/randCity')
def load_randCity():
    return render_template("random-city.html")

@app.route('/randCity/result')
def randCity():
    name = random.randint(0, len(names)-1)
    adj = random.randint(0, len(adjectives)-1)
    year = random.randint(1900, 2024)
    the_string = "{} the {} was born in {} in {}".format(names[name], adjectives[adj], my_city(), year)
    return render_template("random-city-result.html", random_city = the_string)

def my_city():
    conn = psycopg2.connect(host="localhost", port = 5432, database="yangl4", user="yangl4", password="stars929bond")
    
    cur = conn.cursor()
    sql = """SELECT city FROM cities;"""

    cur.execute(sql)

    cities = cur.fetchall()
    idx = random.randint(0, len(cities)-1)
    city = ''+cities[idx][0]

    conn.commit()
    cur.close()
    conn.close()
	
    return city

if __name__ == '__main__':
    my_port = 5137
    app.run(host='0.0.0.0', port = my_port) 
