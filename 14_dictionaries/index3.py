#Python - Change Dictionary Items

#Change Values
print("\nChange Values")
mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)
mydict["year"] = 2018
print(mydict)


#Update Dictionary
print("\nUpdate Dictionary")
mydict.update({"year": 2020})
print(mydict)