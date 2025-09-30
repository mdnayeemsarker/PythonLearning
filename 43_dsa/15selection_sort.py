#Selection Sort with Python

#Selection Sort

# How it works:
  # Go through the array to find the lowest value.
  # Move the lowest value to the front of the unsorted part of the array.
  # Go through the array again as many times as there are values in the array.

#Manual Run Through

#Implement Selection Sort in Python
print("Implement Selection Sort in Python")
mylist = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(mylist)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if mylist[j] < mylist[min_index]:
       min_index = j
  min_value = mylist.pop(min_index)
  mylist.insert(i, min_value)

print(mylist)

#improved Selection Sort algorithm, including swapping values
print("\nImproved Selection Sort algorithm")
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n):
  min_index = i
  for j in range(i+1, n):
     if mylist[j] < mylist[min_index]:
       min_index = j
  mylist[i], mylist[min_index] = mylist[min_index], mylist[i]

print(mylist)