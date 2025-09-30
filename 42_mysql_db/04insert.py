#Python MySQL Insert Into Table

#Insert Into Table
print("Insert Into Table")
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="abmn@!01",
  database="mydatabase"
)
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")


#Insert Multiple Rows
print("\nInsert Multiple Rows")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

#Get the ID of the last inserted row
print("\nGet the ID of the last inserted row")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print("Last inserted ID:", mycursor.lastrowid)