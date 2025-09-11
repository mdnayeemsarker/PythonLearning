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

print('\nNaming Variables')
x = 300
def myfunc():
  x = 200
  print(x)
myfunc()

print(x)

print('\nGlobal Keyword')
def myfunc():
  global x
  x = 300
myfunc()
print(x)

print('\nAnother Example of global keyword')
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)


print('\nNonlocal Keyword')
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())