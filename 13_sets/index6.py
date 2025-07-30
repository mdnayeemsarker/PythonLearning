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