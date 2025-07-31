#Python - Add Dictionary Items 

#Adding Items
print("\nAdding Items")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)
mydict["color"] = "red"
print(mydict)


#Update Dictionary
print("\nUpdate Dictionary")
print(mydict)
mydict.update({"stock": 250})
print(mydict)