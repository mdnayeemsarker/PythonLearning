#Python Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

#Exception Handling
print("Exception Handling\n")
try:
  print(x)
except:
  print("An exception occurred")


#another example
print("\nAnother Example\n")
# print(x)


#Many Exceptions
print("\nMany Exceptions")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


#Else
print("\nElse")

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


#Finally
print("\nFinally")
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#Finally another example
print("\nFinally Another Example")
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")