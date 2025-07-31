#Python - Copy Dictionaries 

#Copy a Dictionary
print("\nCopy a Dictionary")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict1 = mydict.copy()
print(mydict1)


#Another way to make a copy is to use the built-in function dict().
print("\nAnother way to copy a Dictionary")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict1 = dict(mydict)
print(mydict1)