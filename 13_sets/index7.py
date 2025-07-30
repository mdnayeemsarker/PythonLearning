#Python - Set Methods 

#add = 	Adds an element to the set
print("\nadd method")

myset = {"apple", "banana", "cherry"}
myset.add("orange")
print(myset)


#clear = Removes all the elements from the set
print("\nclear")
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)


#copy = Returns a copy of the set
print("\ncopy")
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)


#difference = Returns a set containing the difference between two or more sets
print("\ndifference")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)