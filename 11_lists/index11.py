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

print("\nextend")
mylist.extend(mylist1)
print(mylist)

print("\nindex")
print(mylist1.index("Django"))

print("\ninsert")
mylist1.insert(3, "insert")
print(mylist1)

print("\npop")
mylist1.pop()
print(mylist1)

print("\nremove")
mylist1.remove("insert")
print(mylist1)

print("\nreverse")
mylist1.reverse()
print(mylist1)

print("\nsort")
mylist1.sort()
print(mylist1)