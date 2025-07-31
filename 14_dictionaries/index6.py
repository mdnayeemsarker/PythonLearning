#Python - Loop Dictionaries

#Loop Through a Dictionary
#Print all key names in the dictionary, one by one:
print("\nPrint all key names in the dictionary")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in mydict:
  print(x)


#Print all values in the dictionary, one by one:
print("\nPrint all values in the dictionary, one by one:")
for x in mydict:
  print(mydict[x])


#use the values() method to return values of a dictionary:
print("\nuse the values")
for x in mydict.values():
  print(x)


#You can use the keys() method to return the keys of a dictionary:
print("\nuse the keys")
for x in mydict.keys():
  print(x)


#Loop through both keys and values, by using the items() method:
print("\nLoop through both keys and values")
for x, y in mydict.items():
  print(x, y)