#Python Iterators

#Python Iterators
print('\nPython Iterators')
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().


#Iterator vs Iterable
print('\nIterator vs Iterable')
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print('\nanother')
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#Looping Through an Iterator
print('\nLooping Through an Iterator')
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#another
print('\nanother')
mystr = "banana"

for x in mystr:
  print(x)


#Create an Iterator
print('\nCreate an Iterator')
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))