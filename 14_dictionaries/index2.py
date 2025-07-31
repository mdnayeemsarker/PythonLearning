#Python - Access Dictionary Items

#Accessing Items
print("\nAccessing Items")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict["model"])

#There is also a method called get() that will give you the same result:
print("\nanother way to use get method")
print(mydict.get("model"))

#get keyes only
print("\nget keyes")
print(mydict.keys())


#Get Values
print("\nGet Values")
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change