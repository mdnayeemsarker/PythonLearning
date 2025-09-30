#Python Lists and Arrays

#Creating Lists
print("Creating Lists")
# Empty list
x = []
# List with initial values
y = [1, 2, 3, 4, 5]
# List with mixed types
z = [1, "hello", 3.14, True]

print(x)
print(y)
print(z)

#List Methods
print("\nList Methods")
x = [9, 12, 7, 4, 11]
# Add element:
x.append(8)
# Sort list ascending:
x.sort()
print(x)

#Create Algorithms
print("\nCreate Algorithms")
my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]
for i in my_array:
    print('value:', i)
    if i < minVal:
        minVal = i
print('Lowest value:', minVal)