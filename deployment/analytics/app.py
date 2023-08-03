from flask import Flask, request, jsonify, render_template
import mysql.connector
# import mariadb
import requests
from mysql.connector import pooling

app = Flask(__name__)

# Connect to the MySQL database
# config = mysql.connector.connect(
#     host="35.225.56.175",
#     user="root",
#     password="Password123",
#     database="grades",
#     port=3306,
#     auth_plugin='mysql_native_password'
# )

# config = {
#     "host": "35.225.56.175",
#     "user": "root",
#     "password": "Password123",
#     "database": "grades",
#     "port": 3306,
#     "auth_plugin": 'mysql_native_password'
# }


# mysql_pool = pooling.MySQLConnectionPool(pool_name="mysql_pool", pool_size=20, **config)

# mysql_conn = mysql_pool.get_connection()
# mysql_cursor = mysql_conn.cursor()

# Connect to the MariaDB database
# mariadb_config = mysql.connector.connect(
#     user='root', 
#     password='Password123',
#     host='35.225.56.175', 
#     database='grades',
#     port=3306,
#     auth_plugin='mysql_native_password'
# )

# mconfig = {
#     "host": "35.225.56.175",
#     "user": "root",
#     "password": "Password123",
#     "database": "grades",
#     "port": 3306,
#     "auth_plugin": 'mysql_native_password'
# }
# mariadb_pool = pooling.MySQLConnectionPool(pool_name="mariadb_pool", pool_size=20, **mconfig)

# mariadb_conn = mariadb_pool.get_connection()
# mariadb_cursor = mariadb_conn.cursor()

def Average(lst):
    return sum(lst) / len(lst)

@app.route('/write', methods=['POST'])
def write_data():
    config = {
    "host": "35.225.56.175",
    "user": "root",
    "password": "Password123",
    "database": "grades",
    "port": 3306,
    "auth_plugin": 'mysql_native_password'
    }


    mysql_pool = pooling.MySQLConnectionPool(pool_name="mysql_pool", pool_size=20, **config)

    mysql_conn = mysql_pool.get_connection()
    mysql_cursor = mysql_conn.cursor()

    mconfig = {
    "host": "35.225.56.175",
    "user": "root",
    "password": "Password123",
    "database": "grades",
    "port": 3306,
    "auth_plugin": 'mysql_native_password'
    }
    mariadb_pool = pooling.MySQLConnectionPool(pool_name="mariadb_pool", pool_size=20, **mconfig)
    mariadb_conn = mariadb_pool.get_connection()
    mariadb_cursor = mariadb_conn.cursor()

    data = request.get_json()
    studentid = data.get('studentid')
    # Execute a SELECT statement on the MySQL database
    mysql_cursor.execute("SELECT * FROM grades.Students WHERE studentid = %s", (studentid, ))
    rows = mysql_cursor.fetchall()


    for row in rows:
        # Get values from the result
        id = row[0]
        lastname = row[1]
        firstname = row[2]
        acit3895 = row[3]
        acit4850 = row[4]
        acit4880 = row[5]
        acit4640 = row[6]
        acit4630 = row[7]

        grades = [acit3895, acit4850, acit4880, acit4640, acit4630]

        #calculations
        max_grade = int(max(grades))
        min_grade = int(min(grades))
        average_grade = int(round(Average(grades)))
        
        # # Write the data to the MariaDB database
        # mariadb_cursor.execute("INSERT INTO grades.Stats (studentID, lastname, firstname, max_grade, min_grade, average_grade) VALUES (%s, %s, %s, %s, %s, %s)", (id, lastname, firstname, max_grade, min_grade, average_grade))
        # #mariadb_cnx.commit()

        # mariadb_conn.close()

        mariadb_cursor.execute("INSERT INTO grades.Stats (studentID, lastname, firstname, max_grade, min_grade, average_grade) VALUES (%s, %s, %s, %s, %s, %s)", (id, lastname, firstname, max_grade, min_grade, average_grade))
        
    mariadb_conn.commit()
    mariadb_cursor.close()
    mariadb_conn.close()

    mysql_cursor.close()
    mysql_conn.close()
        
    return "Data written successfully!"

if __name__ == '__main__':
    app.run(port=4001, host=('0.0.0.0'))



