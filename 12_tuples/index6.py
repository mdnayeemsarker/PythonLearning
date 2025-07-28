#Python - Tuple Methods

#count = Returns the number of times a specified value occurs in a tuple
print("\ncount")
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
x = tuple3.count(2)
print(x)


#index = Searches the tuple for a specified value and returns the position of where it was found
print("\nindex")
x = tuple3.index(2)

print(x)