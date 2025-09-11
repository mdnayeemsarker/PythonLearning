#Python Modules

#Consider a module to be the same as a code library.
#A file containing a set of functions you want to include in your application.
print('\nCreate a Module')
import newmodule 
def greeting(name):
  print("Hello, " + name)
newmodule.greeting("Jonathan")

print('\nVariables in Module')
a = newmodule.person1["age"]
print(a)