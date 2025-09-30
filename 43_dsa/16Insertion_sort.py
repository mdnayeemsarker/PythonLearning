#Insertion Sort with Python

#Insertion Sort

# How it works:
  # Take the first value from the unsorted part of the array.
  # Move the value into the correct place in the sorted part of the array.
  # Go through the unsorted part of the array again as many times as there are values.

#Manual Run Through

#Implement Insertion Sort in Python

# To implement the Insertion Sort algorithm in a Python program, we need:

# An array with values to sort.
# An outer loop that picks a value to be sorted. For an array with n values, this outer loop skips the first value, and must run n - 1 times.
# An inner loop that goes through the sorted part of the array, to find where to insert the value. If the value to be sorted is at index i, the inner loop must run i the sorted part of the array starts at index 0 and ends at index i - 1. 

print("Implement Insertion Sort in Python")
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist.pop(i)
  for j in range(i-1, -1, -1):
    if mylist[j] > current_value:
      insert_index = j
  mylist.insert(insert_index, current_value)

print(mylist)

#Insert the improvements in the sorting algorithm
print("\nImproved Insertion Sort algorithm")
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist[i]
  for j in range(i-1, -1, -1):
     if mylist[j] > current_value:
       mylist[j+1] = mylist[j]
       insert_index = j
     else:
       break
  mylist[insert_index] = current_value

print(mylist)