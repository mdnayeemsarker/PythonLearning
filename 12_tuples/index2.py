#Python - Update Tuples 

#Change Tuple Values
print("\nChange Tuple Values")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#Add Items
mytuple = ("apple", "banana", "cherry")
y = list(mytuple)
y.append("orange")
mytuple = tuple(y)
print(mytuple)

y = ("pumkin",)
mytuple += y
print(mytuple)


#Remove Items
y = list(mytuple)
y.remove("apple")
mytuple = tuple(y)
print(mytuple)

#Or delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)