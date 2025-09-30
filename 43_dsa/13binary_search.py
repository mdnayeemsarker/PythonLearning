#Binary Search with Python

# How it works:
  # Check the value in the center of the array.
  # If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
  # Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
  # If the value is found, return the target value index. If the target value is not found, return -1.

#Implementing Binary Search in Python

# To implement the Binary Search algorithm we need:
  # An array with values to search through.
  # A target value to search for.
  # A loop that runs as long as left index is less than, or equal to, the right index.
  # An if-statement that compares the middle value with the target value, and returns the index if the target value is found.
  # An if-statement that checks if the target value is less than, or larger than, the middle value, and updates the "left" or "right" variables to narrow down the search area.
  # After the loop, return -1, because at this point we know the target value has not been found.

print("Implementing Binary Search in Python")
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")