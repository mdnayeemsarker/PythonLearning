#Python - List Methods

#List Methods
oldlist = ["html", "css", "bootstrap", "php", "python"]
mylist = ["Laravel", "flask", "Django"]
mylist1 = ["Laravel", "flask", "Django", "flask", "flask"]

print("\nappend")
mylist.append(oldlist[2])
print(mylist)

print("\nclear")
mylist.clear()
print(mylist)

print("\ncopy")
mylist = mylist1.copy()
print(mylist)

print("\ncount")
print(mylist.count("flask"))