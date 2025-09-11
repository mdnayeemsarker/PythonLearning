#Local Scope

#A variable created inside a function is available inside that function:
print('\nA variable created inside a function is available inside that function:')
def myfunc():
  x = 300
  print(x)

myfunc()

print('\nFunction Inside Function')
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

print('\nGlobal Scope')
x = 300
def myfunc():
  print(x)

myfunc()
print(x)