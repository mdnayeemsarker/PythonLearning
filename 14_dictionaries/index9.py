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