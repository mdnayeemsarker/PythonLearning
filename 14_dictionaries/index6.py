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