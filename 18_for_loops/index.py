#Python For Loops

#Python has two primitive loop commands:
  # while loops
  # for loops

#Python For Loops
print("\nPython For Loops")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#Looping Through a String
print("\nLooping Through a String")
for x in "banana":
  print(x)


#The break Statement
print("\nThe break Statement")
for x in fruits:
  print(x)
  if x == "banana":
    break


#The continue Statement
print("\nThe continue Statement")
for x in fruits:
  if x == "banana":
    continue
  print(x)


#The range Function
print("\nThe range Function")
for x in range(6):
  print(x)

#another range 2
print("\nanother range")
for x in range(2, 6):
  print(x)

#another range 3
print("\nanother range")
for x in range(2, 30, 3):
  print(x)


#Else in For Loop
print("\nElse in For Loop")
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#Else with range
print("\nElse with range")
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#Nested Loops
print("\nNested Loops")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


#The pass Statement
print("\nThe pass Statement")
for x in [0, 1, 2]:
  pass