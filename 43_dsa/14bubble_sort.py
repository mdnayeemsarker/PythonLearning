#Bubble Sort with Python

#Bubble Sort

# How it works:
  # Go through the array, one value at a time.
  # For each value, compare the value with the next value.
  # If the value is higher than the next one, swap the values so that the highest value comes last.
  # Go through the array as many times as there are values in the array.

#Manual Run Through

#Implement Bubble Sort in Python
print("Implement Bubble Sort in Python")
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)

#Improved Bubble Sort algorithm
print("\nImproved Bubble Sort algorithm")
mylist = [7, 3, 9, 12, 11]

n = len(mylist)
for i in range(n-1):
  swapped = False
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
      swapped = True
  if not swapped:
    break

print(mylist)