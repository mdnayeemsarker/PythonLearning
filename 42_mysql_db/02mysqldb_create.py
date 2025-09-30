#Python MySQL Create Database

#Creating a Database

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
print(mydb)

# Check if Database Exists
print("show databases")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# check if database exists is connected to mysql or not
print("\ncheck if database exists is connected to mysql or not")
mydatabase = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01",
  database="mydatabase"
)

print(mydatabase)