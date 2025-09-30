#DSA Merge Sort with Python

#Merge Sort

# How it works: 
  # Divide the unsorted array into two sub-arrays, half the size of the original.
  # Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
  # Merge two sub-arrays together by always putting the lowest value first.
  # Keep merging until there are no sub-arrays left.

#Manual Run Through

# Implement Merge Sort in Python
print("Implement Merge Sort in Python")
def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)