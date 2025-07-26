# Python Booleans


#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

#run a condition in an if statement, Python returns True or False:
a = 255
b = 50
print("\n")
if a > b :
    print("a is bigger than b")
else:
    print("b is bigger than b")


#Evaluate Values and Variables
print("\n")
print(bool("Nayeem"))
print(bool(25))

print("\n")
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#Most Values are True
print("\nMost Values are true")
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#Some Values are False
print("\nSome Values are False")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myClass():
    def __len__(self):
        return 0
    
myObject = myClass()
print(bool(myObject))

#Functions can Return a Boolean
print("\nFunctions can Return a Boolean")

def myFunction():
    return True

print(myFunction())