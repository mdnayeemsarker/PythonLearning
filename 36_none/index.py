#Python None
print("Python None")
x = None
print(x)

#None Type
print("\nNone Type")
x = None
print(type(x))

#Comparing to None
print("\nComparing to None")
x = None
if x is None:
  print("Yes, x is None")
else:
  print("No, x is not None")

#Comparing to None another example
print("\nComparing to None another example")
result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")

#True or False
print("\nTrue or False")
print(bool(None))

#Functions returning None
print("\nFunctions returning None")
def myfunc():
  x = 5

x = myfunc()
print(x)