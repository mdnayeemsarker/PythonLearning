#Python - Update Tuples 

#Change Tuple Values
print("\nChange Tuple Values")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)