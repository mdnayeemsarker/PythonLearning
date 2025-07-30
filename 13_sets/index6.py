#Python - Join Sets

#Join Sets
print("\nJoin Sets")

myset = {"apple", "banana", "cherry"}
set1 = {1, 2, 3}
set2 = myset.union(set1)
print(set2)

#You can use the | operator instead of the union() method, and you will get the same result.
set3 = myset | set1
print(set3)


#Join Multiple Sets
print("\nJoin Multiple Sets")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#another way to use operator
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)


#Join a Set and a Tuple
print("\nJoin a Set and a Tuple")
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


#Update
print("\nUpdate")
set1.update(set2)
print(set1)


#Intersection = The intersection() method will return a new set, that only contains the items that are present in both sets.
print("\nIntersection")
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)