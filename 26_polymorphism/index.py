#Python Polymorphism

#Function Polymorphism
print('\nFunction Polymorphism')
# An example of a Python function that can be used on different objects is the len() function.
print('\nstring')
#String = For strings len() returns the number of characters:
x = "Hello World!"
print(len(x))


#Tuple
print('\nTuple')
# For tuples len() returns the number of items in the tuple:
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

#Dictionary
print('\nDictionary')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))