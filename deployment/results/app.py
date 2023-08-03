from flask import Flask, request, jsonify, render_template, redirect
import requests
import mysql.connector
from mysql.connector import pooling

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET'])
def webpage():
    #check if its web or 127.0.0.1
    return redirect('http://146.148.102.55:9000/passcheck')

@app.route('/check', methods=['POST'])
def checkpass():
    username = request.form["username"]
    password = request.form["password"]

    # Perform authentication checks
    if username == 'user' and password == 'pass':
        return render_template("templates/index.html")
    else:
        return jsonify({'message': 'Authentication failed'}), 401

@app.route('/results', methods=['POST'])
def index():
    # Connect to the database
    # config = mysql.connector.connect(
    #     host="35.225.56.175",
    #     user="root",
    #     password="Password123",
    #     database="grades",
    #     port=3306,
    #     auth_plugin='mysql_native_password'
    # )

    config = {
    "host": "35.225.56.175",
    "user": "root",
    "password": "Password123",
    "database": "grades",
    "port": 3306,
    "auth_plugin": 'mysql_native_password'
    }

    mysql_pool = pooling.MySQLConnectionPool(pool_name="mysql_pool", pool_size=5, **config)
    mysql_conn = mysql_pool.get_connection()
    cursor = mysql_conn.cursor()

    studentid = request.form["studentid"]

    # Retrieve data from the database
    # query = "SELECT * FROM Stats WHERE studentid = '%s'"
    # cursor.execute(query, (studentid))

    cursor.execute("SELECT * FROM grades.Stats WHERE studentid = %s", (studentid, ))

    rows = cursor.fetchone()

    # Close the connection
    # cursor.close()
    # conn.close()

    # Render the HTML template and pass the data to it
    return render_template("templates/stats.html", rows=rows)

if __name__ == '__main__':
    app.run(port=4002, host=('0.0.0.0'))
