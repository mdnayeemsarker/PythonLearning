#Python - Sort Lists 

#Sort List Alphanumerically
print("\nSort List Alphanumerically")
myalist = ["apple", "banana", "cherry", "1apple", "2banana", "3cherry"]
myalist.sort()
print(myalist)


#Sort List Numerically
print("\nSort the list numerically")
mynlist = [100, 50, 65, 82, 23]
mynlist.sort()
print(mynlist)


#Sort Descending
print("\nSort Descending")
myadlist = ["apple", "banana", "cherry", "1apple", "2banana", "3cherry"]
myadlist.sort(reverse=True)
print(myadlist)

myndlist = [100, 50, 65, 82, 23]
myndlist.sort(reverse=True)
print(myndlist)


#Customize Sort Function
print("\nCustomize Sort Function")

def myfunc(n):
    return abs(n - 50)

myndlist = [100, 50, 65, 82, 23]
myndlist.sort(key = myfunc)
print(myndlist)