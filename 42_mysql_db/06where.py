#Python MySQL Where

#Select With a Filter
print("Select With a Filter")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Highway 21", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Wildcard Characters
print("\nWildcard Characters")
sql = "SELECT * FROM customers WHERE address LIKE '%hway%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Prevent SQL Injection
print("\nPrevent SQL Injection")
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)