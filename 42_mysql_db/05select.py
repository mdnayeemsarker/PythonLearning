#Python MySQL Select From

#Select From a Table
print("Select From a Table")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Selecting Columns
print("\nSelecting Columns")
mycursor.execute("SELECT address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)