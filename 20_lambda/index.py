#Python Lambda

#Lambda
print('\nnLambda')
x = lambda a : a + 10
print(x(5))

#another
x = lambda a, b : a * b
print(x(5, 6))


#Why Use Lambda Functions?

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

print('\nWhy Use Lambda Functions?')
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
#Use that function definition to make a function that always doubles the number you send in:
print(mydoubler(11))


#Or, use the same function definition to make a function that always triples the number you send in:
print('\nuser same function defination')
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))