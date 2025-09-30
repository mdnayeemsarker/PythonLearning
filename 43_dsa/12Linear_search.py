#Linear Search with Python

# How it works:
  # Go through the array value by value from the start.
  # Compare each value to check if it is equal to the value we are looking for.
  # If the value is found, return the index of that value.
  # If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.

#Implement Linear Search in Python
print("Implement Linear Search in Python")
mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

if 4 in mylist:
  print("Found!")
else:
  print("Not found!")

#But if you need to find the index of a value, you will need to implement a linear search
print("\nLinear Search to find the index of a value")
def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

result = linearSearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")