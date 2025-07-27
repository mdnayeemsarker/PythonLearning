#Python - Remove List Items Remove Specified Item

#Remove Specified Item
print("\nAppend Items")

mylist = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
mylist.remove("banana")
print(mylist)


#Remove Specified Index
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)

#The del keyword also removes the specified index:
del mylist[0]
print(mylist)

del mylist