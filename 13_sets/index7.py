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


#difference_update = Removes the items in this set that are also included in another, specified set
print("\ndifference_update")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)


#discard = Remove the specified item
print("\ndiscard")
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)


#intersection = Returns a set, that is the intersection of two other sets
print("\nintersection")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


#intersection_update = Removes the items in this set that are not present in other, specified set(s)
print("\nintersection_update")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)


#isdisjoint = Returns whether two sets have a intersection or not
print("\nisdisjoint")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)


#issubset = Returns True if all items of this set is present in another set
print("\nissubset")
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)


#issuperset = Returns True if all items of another set is present in this set
print("\nissuperset")
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


#pop = Removes an element from the set
print("\npop")
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)


#remove = Removes the specified element
print("\nremove")
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)


#symmetric_difference = Returns a set with the symmetric differences of two sets
print("\nsymmetric_difference")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


#symmetric_difference_update = Inserts the symmetric differences from this set and another
print("\nsymmetric_difference_update")
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)