#Python If ... Else

#Python Conditions and If statements
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

print("\nIf statement:")
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Indentation
# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error


#Elif
print("\nElif")
c = 33
d = 33
if c > d:
  print("b is greater than a")
elif c == d:
  print("a and b are equal")


#Else
print("\nElse")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#example without elif
print("\nexample without elif")
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#Short Hand If
print("\nShort Hand If")
if a > b: print("a is greater than b")