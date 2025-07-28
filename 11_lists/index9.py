#Python - Copy Lists

#Copy a List
print("\nCopy a List")
oldlist = ["html", "css", "bootstrap", "php", "python"]
print(oldlist)
mylist = oldlist.copy()
print(mylist)


#Use the list method
print("\nUse the list method")
mylist = list(oldlist)
print(mylist)


#Use the slice Operator
print("\nUse the slice Operator")
mylist = oldlist[:]
print(mylist)