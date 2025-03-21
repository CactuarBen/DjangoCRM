import os

import mysql.connector

database = mysql.connector.connect(

    host='127.0.0.1',
    user='root',
    passwd='19661998',

)

# prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS mydb")

print("All Done!")
