#Python Tuples

#Tuple
print("\nTuple")
mytuple = ("apple", "banana", "cherry")
print(mytuple)


#Allow Duplicates
print("\nAllow Duplicates")

mytuple = ("apple", "banana", "cherry", "apple", "cherry")
print(mytuple)


#Tuple Length
print("\nTuple Length")
print(len(mytuple))


#Create Tuple With One Item
print("\nCreate Tuple With One Item")
mytupleo = ("apple",)
mytupleo1 = ("apple")
print(type(mytupleo))
print(type(mytupleo1))


#Tuple Items - Data Types
print("\nTuple Items - Data Types")
strtouple = ("apple", "banana", "cherry", "apple", "cherry")
inttouple = (25,36,48,96,54)
booltouple = (True, False, False, True)
print(type(strtouple))
print(type(inttouple))
print(type(booltouple))

#A tuple can contain different data types
print("\nA tuple can contain different data types")
mytupled = ("nayeem", "asha", 25, 129943, False, True, True)
print(type(mytupled))