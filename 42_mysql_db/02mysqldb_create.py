#Python MySQL Create Database

#Creating a Database

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase")
print(mydb)