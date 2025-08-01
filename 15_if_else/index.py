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


#Short Hand If ... Else
print("\nShort Hand If ... Else")
a = 2
b = 330
print("A") if a > b else print("B")


#One line if else statement, with 3 conditions:
print("\nOne line if else statement, with 3 conditions")
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#And
print("\nAnd")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


#Or
print("\nOr")
if a > b or a > c:
  print("At least one of the conditions is True")

#Not
print("\nNot")
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")