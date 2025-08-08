#Python Class/Objects

#Class
print('\nClass')
class MyClass:
  x = 5

print(MyClass)


#Object
print('\nObject')
p1 = MyClass()
print(p1.x)


#The __init__() Method
print('\nThe __init__() Method')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)