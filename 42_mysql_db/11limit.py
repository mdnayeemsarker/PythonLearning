#Python MySQL Limit

#Limit the Result
print("Limit the Result")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 15")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Start From Another Position
print("\nStart From Another Position")
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)