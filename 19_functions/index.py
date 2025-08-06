#Python Functions

#Creating a Function
print("\nCreating a Function")

def my_function():
  print("Hello from a function")


#Calling a Function
print("\nCalling a Function")
my_function()


#Arguments
print("\nArguments")
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")


#Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.


#Number of Arguments
print("\nNumber of Arguments")
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")


#Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#Keyword Arguments
print ("\nKeyword Arguments")
def my_function1(child3, child2, child1):
  print("The youngest child is " + child3)

my_function1(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Arbitrary Keyword Arguments, **kwargs
print('\nArbitrary Keyword Arguments, **kwargs')
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")


#Default Parameter Value
print('\nDefault Parameter Value')
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#Passing a List as an Argument
print('\nPassing a List as an Argument')
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#Return Values
print('\nReturn Values')
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))