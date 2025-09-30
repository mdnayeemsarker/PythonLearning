#Python MySQL Create Table

#Creating a Table
print("Creating a Table")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01",
  database="mydatabase"
)
mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
print(mydb)

#Check if Table Exists
print("\ncheck if table exists is connected to mysql or not")
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
