#Hash Tables with Python

#Hash Table
#Building A Hash Table from Scratch
#To get the idea of what a Hash Table is, let's try to build one from scratch, to store unique first names inside it.
#We will build the Hash Table in 5 steps:

  #Create an empty list (it can also be a dictionary or a set).
  #Create a hash function.
  #Inserting an element using a hash function.
  #Looking up an element using a hash function.
  #Handling collisions.

#Step 1: Create an Empty List
my_list = [None, None, None, None, None, None, None, None, None, None]
# Step 2: Create a Hash Function
def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

print("'Bob' has hash code:", hash_function('Bob'))

#Step 3: Inserting an Element
def add(name):
  index = hash_function(name)
  my_list[index] = name

add('Bob')
print(my_list)

my_list = [None, None, None, None, None, None, None, None, None, None]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def add(name):
  index = hash_function(name)
  my_list[index] = name

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)

#Step 4: Looking up a name
my_list = [None, None, None, None, None, None, None, None, None, None]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def add(name):
  index = hash_function(name)
  my_list[index] = name

def contains(name):
  index = hash_function(name)
  return my_list[index] == name

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print("'Pete' is in the Hash Table:", contains('Pete'))

#Step 5: Handling collisions
my_list = [
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  [],
  []
]

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def add(name):
  index = hash_function(name)
  my_list[index].append(name)

def contains(name):
  index = hash_function(name)
  return my_list[index] == name

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list)
