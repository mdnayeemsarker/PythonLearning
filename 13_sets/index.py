#Python Sets

#Set
print("\nSet")

myset = {"apple", "banana", "cherry"}
print(myset)


#Duplicates Not Allowed
print("\nDuplicates Not Allowed")
myset = {"apple", "banana", "cherry", "apple"}
print(myset)

#consider the same value
myset = {"apple", "banana", "cherry", True, 1, 2}
print(myset)


#Get the Length of a Set
print("\nGet the Length of a Set")
print(len(myset))


#Set Items - Data Types
print("\nSet Items - Data Types")
strset = {"apple", "banana", "cherry"}
intset = {1, 5, 7, 9, 3}
boolset = {True, False, False}
print(strset)
print(intset)
print(boolset)

print("\nset data type")
print(type(strset))
print(type(intset))
print(type(boolset))


#The set Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)