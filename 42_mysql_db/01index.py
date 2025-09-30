#Python MySQL

#MySql Database

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01"
)

print(mydb)