#Python - Access Tuple Items

#Access Tuple Items
print("\nAccess Tuple Items")
mytuple = ("apple", "banana", "cherry")
print(mytuple[2])


#Negative Indexing
print("\nNegative Indexing")
mytuple = ("apple", "banana", "cherry")
print(mytuple[-1])


#Range of Indexes
print("\nRange of Indexes")
mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(mytuple[2:5])

print(mytuple[:4])
print(mytuple[4:])


#Range of Negative Indexes
print("\nRange of Negative Indexes")
print(mytuple[-4:-1])


#Check if Item Exists
print("\nCheck if Item Exists")
if "apple" in mytuple:
  print("Yes, 'apple' is in the fruits tuple")