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


#Naming a Module
# You can name the module file whatever you like, but it must have the file extension .py 
# Re-naming a Module
# You can create an alias when you import a module, by using the as keyword:
print('\nNaming a Module')
import newmodule as mx

print('\nRe-naming a Module')
a = mx.person1["name"]
print(a)
