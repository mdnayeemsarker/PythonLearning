#Python - Dictionary Methods

#clear = 	Removes all the elements from the dictionary
print("\nclear")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)


#copy = Returns a copy of the dictionary
print("\ncopy")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)


#fromkeys = Returns a dictionary with the specified keys and value
print("\nfromkeys")
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)


#get = Returns the value of the specified key
print("\nget")
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)