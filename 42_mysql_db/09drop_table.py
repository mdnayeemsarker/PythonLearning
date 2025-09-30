#Python MySQL Drop Table

#Delete a Table
print("Delete a Table")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "DROP TABLE customers1"
mycursor.execute(sql)
print("Table Deleted")