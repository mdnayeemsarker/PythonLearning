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


#Primary Key
print("\nPrimary Key")
# mycursor.execute("CREATE TABLE customers1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
print("Table with Primary Key created.")

#Create primary key on an existing table
print("\nCreate primary key on an existing table")
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
print("Primary Key created on existing table.")