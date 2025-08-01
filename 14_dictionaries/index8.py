#Python - Nested Dictionaries

#Nested Dictionaries
print("\nNested Dictionaries")
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)

#Another way 
print("\nAnother Way")
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)


#Access Items in Nested Dictionaries
print("\nAccess Items in Nested Dictionaries")
print(myfamily["child2"]["name"])


#Loop Through Nested Dictionaries
print("\nLoop Through Nested Dictionaries")
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])