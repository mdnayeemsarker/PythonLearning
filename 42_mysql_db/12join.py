#Python MySQL Join

#Join Two or More Tables
print("Join Two or More Tables")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01",
  database="mydatabase"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT customers.name, customers1.color, customers1.amount FROM customers JOIN customers1 ON customers.id = customers1.customer_id")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# LEFT JOIN
print("\nLEFT JOIN")
sql = "SELECT customers.name AS user, customers1.color AS favorite FROM customers LEFT JOIN customers1 ON customers.id = customers1.customer_id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)