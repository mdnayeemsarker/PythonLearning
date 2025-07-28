#Python - Loop Tuples Loop Through a Tuple

#Loop Through a Tuple
print("\nLoop Through a Tuple")
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)


#Loop Through the Index Numbers
print("\nLoop Through the Index Numbers")
for i in range(len(mytuple)):
  print(mytuple[i])


#Using a While Loop
print("\nUsing a While Loop")
i = 0
while i < len(mytuple):
  print(mytuple[i])
  i = i + 1