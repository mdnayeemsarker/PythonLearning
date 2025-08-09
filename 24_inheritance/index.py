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