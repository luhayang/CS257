# What is in this file
#
# author: Matt Lepinski
#

'''
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
'''
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__, 
        static_url_path='',
        static_folder='static',
        template_folder='templates')

'''
def test_func():
    return app.send_static_file('NovoVoom.html')
'''
# To test hompage
# http://stearns.mathcs.carleton.edu:1234/
@app.route('/')
def load_hompage():
    return app.send_static_file('hompage.html')

'''
def internal():
    return render_template('pages.html')
'''
@app.route('/internal')
def load_internal_pages():
    return render_template('internal-pages.html')

@app.route('/internal/')
def redirect_me():
    return redirect(url_for('internal'))

'''
def info_tech():
    return render_template('info_tech.html')
'''
@app.route('/internal/it')
def load_info_tech():
    return render_template('info_tech.html')

'''
def direct_form():
    return render_template('direct_form.html')
'''
@app.route('/internal/directory')
def load_direct_form():
    return render_template('direct_form.html')

'''
@app.route('/internal/submit', methods = ['POST'])
def direct_submit():
    cnx = mysql.connector.connect(user='webapp', password='novovoom1web', host='db', database='NovoVoom')
    cursor = cnx.cursor(buffered=True)
    form_data = request.form
    last_name = form_data['last']


    query = "SELECT first, last, dept, phone FROM Employee WHERE last = '" + last_name + "'";
    
    q_list = query.split(';')

    for q in q_list:
        if (len(q) > 2):
            cursor.execute(q) 

    cnx.commit()

    output_str = ""
    for data in cursor:
        for item in data:
            output_str = output_str + str(item) + ",   "
        output_str = output_str + "\n"

    return render_template('results.html', output = output_str)
'''
    
# Search function for Employee Directory
@app.route('/internal/submit', methods = ['POST'])
def directory_form_submit():
    cnx = mysql.connector.connect(user='webapp', password='novovoom1web', host='db', database='NovoVoom')
    cursor = cnx.cursor(buffered=True)
    form_data = request.form
    last_name = form_data['last']

    search_results = search_diectory(cnx, cursor, last_name)
    return render_template('results.html', output = search_results)

# Searh cof a last name in the database
def search_diectory(db_cnx, db_cusor, last_name):
    sql_query = "SELECT first, last, dept, phone FROM Employee WHERE last = '" + last_name + "';"
    
    # When having multiple queries in one line
    sql_query_list = sql_query.split(';')
    for query in sql_query_list:
        if (len(query) > 2):
            db_cusor.execute(query) 

    db_cnx.commit()

    output_str = ""
    for data in db_cusor:
        for item in data:
            output_str = output_str + str(item) + ",   "
        output_str = output_str + "\n"
    
    return output_str

app.run(host='0.0.0.0', port=5137)
