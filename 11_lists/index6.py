#Python - Loop Lists 

#Loop Through a List
print("\nLoop Through a List")

mylist = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
for x in mylist:
  print(x)


#Loop Through the Index Numbers
print("\nLoop Through the Index Numbers")
for i in range(len(mylist)):
  print(mylist[i])


#Using a While Loop
print("\nUsing a While Loop")
mywlist = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
i = 0
while i < len(mywlist):
  print(mywlist[i])
  i = i + 1