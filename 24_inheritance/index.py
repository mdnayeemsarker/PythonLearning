#Python Inheritance

#Python Inheritance
print('\nPython Inheritance')
#create parent class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

xp = Person("John", "Doe")
xp.printname()

#Use the Person class to create an object, and then execute the printname method:

#create child class
class Student(Person):
  pass

xs = Student("Mike", "Olsen")
xs.printname()



#Add the __init__() Function
print('\nAdd the __init__() Function')
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()



#Use the super() Function
print('\nUse the super() Function')
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  
  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

x = Student("Nayeem", "Sarker")
x.printname()



#Add Properties
print('\nAdd Properties')
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2020
x = Student("Nayeem", "Sarker")
print(x.graduationyear)



#Add Methods
print('\nAdd Methods')
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2020

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Nayeem", "Sarker")
x.welcome()