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


#The __str__() Method
print('\nThe __str__() Method')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)


#another
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)


#Create Methods
print('\nCreate Methods')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


#The self Parameter
print('\nThe self Parameter')
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()


#Modify Object Properties
print('\nModify Object Properties')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40
print(p1.age)


#Delete Object Properties
print('\nDelete Object Properties')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age
# print(p1.age)


#Delete Objects
print('\nDelete Objects')
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
# print(p1)
