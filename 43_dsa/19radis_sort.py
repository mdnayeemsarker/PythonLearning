#DSA Radix Sort with Python

#Radix Sort

# How it works: 
  # Start with the least significant digit (rightmost digit).
  # Sort the values based on the digit in focus by first putting the values in the correct bucket based on the digit in focus, and then put them back into array in the correct order.
  # Move to the next digit, and sort again, like in the step above, until there are no digits left.

#Manual Run Through

# Implement Radix Sort in Python
print("Implement Radix Sort in Python")
mylist = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", mylist)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(mylist)
exp = 1

while maxVal // exp > 0:

  while len(mylist) > 0:
    val = mylist.pop()
    radixIndex = (val // exp) % 10
    radixArray[radixIndex].append(val)

  for bucket in radixArray:
    while len(bucket) > 0:
      val = bucket.pop()
      mylist.append(val)

  exp *= 10

print(mylist)