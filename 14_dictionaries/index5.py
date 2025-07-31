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