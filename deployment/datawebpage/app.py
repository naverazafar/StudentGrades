from flask import Flask, request, jsonify, render_template
import requests
import mysql.connector
from mysql.connector import pooling

app = Flask(__name__, template_folder='.')

@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    auth = data.get('auth')

    if auth:
        # If authentication is successful, display the web page
        response = render_template("templates/welcome.html")
        return response
    else:
        return jsonify({'message': 'Authentication failed'}), 401

@app.route('/submit', methods=['POST'])
def submit():
    studentid = int(request.form["studentid"])
    lastname = request.form["lastname"]
    firstname = request.form["firstname"]
    acit3895 = int(request.form["acit3895"])
    acit4850 = int(request.form["acit4850"])
    acit4880 = int(request.form["acit4880"])
    acit4640 = int(request.form["acit4640"])
    acit4630 = int(request.form["acit4630"])

    # Connect to the database and write the form data to a table
    # Code to connect to the database and insert the form data goes here

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

    # Write the form data to the database
    mysql_conn = mysql_pool.get_connection()
    cursor = mysql_conn.cursor()
    cursor.execute("INSERT INTO grades.Students (studentid, lastname, firstname, acit3895, acit4850, acit4880, acit4640, acit4630) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)", (studentid, lastname, firstname, acit3895, acit4850, acit4880, acit4640, acit4630))
    mysql_conn.commit()
    cursor.close()

    response = requests.post("http://34.135.111.54:4001/write", json={'studentid': studentid})

    if response.status_code == 200:
        return "Form Submitted Successfully"
    else:
        return "Error submitting form"


if __name__ == '__main__':
    app.run(port=2000, host=('0.0.0.0'))
