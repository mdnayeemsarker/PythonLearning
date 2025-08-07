#Python Arrays

#Arrays
print('\nArrays')
cars = ["Ford", "Volvo", "BMW"]
print(cars)


#Access the Elements of an Array
print('\nAccess the Elements of an Array')
print(cars[1])


#The Length of an Array
print('\nThe Length of an Array')
print(len(cars))


#Looping Array Elements
print('\nLooping Array Elements')
for x in cars:
  print(x)


#Adding Array Elements
print('\nAdding Array Elements')
cars.append("Honda")
print(cars)


#Removing Array Elements
print('\nRemoving Array Elements')
cars.pop(1)
print(cars)



#Array Methods
print('\nArray Methods')
#append = Adds an element at the end of the list
print('\nappend')
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")


#clear = Removes all the elements from the list
print('\nclear')
fruits.clear()
print(fruits)


#copy = Returns a copy of the list
print('\ncopy')
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)


#count = Returns the number of elements with the specified value
print('\ncount')
x = fruits.count("cherry")
print(x)


#extend = Add the elements of a list (or any iterable), to the end of the current list
print('\nextend')
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)


#index = Returns the index of the first element with the specified value
print('\nindex')
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)


#insert = Adds an element at the specified position
print('\ninsert')
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)


#pop = Removes the element at the specified position
print('\npop')
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)