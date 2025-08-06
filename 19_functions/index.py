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