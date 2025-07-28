#Python - Join Lists Join Two Lists

#Join Two Lists
print("\nJoin Two Lists")
oldlist = ["html", "css", "bootstrap", "php", "python"]
mylist = ["Laravel", "flask", "Django"]
print(oldlist, mylist)
oldlist = oldlist + mylist
print(oldlist)


#Another way to join two lists is by appending all the items from list2 into list1, one by one:
print("\nanother way to join")
oldlist = ["html", "css", "bootstrap", "php", "python"]
mylist = ["Laravel", "flask", "Django"]
for x in oldlist:
    mylist.append(x)
print(mylist)


#join list with extend method
print("\njoin list with extend method")
oldlist = ["html", "css", "bootstrap", "php", "python"]
mylist = ["Laravel", "flask", "Django"]
mylist.extend(oldlist)
print(mylist)