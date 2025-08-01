#Python Dictionaries

#Dictionary
print("\nDictionary")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)


#Dictionary Items
print("\nDictionary Items")
print(mydict["brand"])

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
print("\nDuplicates Not Allowed")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(mydict)


#Dictionary Length
print("\nDictionary Length")
print(len(mydict))


#Dictionary Items - Data Types
print("\nDictionary Items - Data Types")
mydict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(mydict))


#Dictionary Constructor
print("\nDictionary Constructor")
mydict = dict(name = "John", age = 36, country = "Norway")
print(mydict)