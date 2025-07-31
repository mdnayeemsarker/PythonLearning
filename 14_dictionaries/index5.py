#Python - Remove Dictionary Items Removing Items

#Removing Items
print("\nRemoving Items")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)
mydict.pop("year")
print(mydict)

#popitem = The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
print("\npopitem")
mydict.popitem()
print(mydict)

#The del keyword removes the item with the specified key name:
print("\nDel keyword")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del mydict["model"]
print(mydict)


#The del keyword can also delete the dictionary completely:
print("\ndel keyword also delete the dictionary")
del mydict
print(mydict)