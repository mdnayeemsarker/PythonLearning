#Python RegEx

#RegEx Module

print('\nRegEx Module')
import re

#RegEx in Python
print('\nRegEx in Python')
#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")


#The findall() Function
print('\nThe findall Function')
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

#Another example
print('\nAnother Example')
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


#The search() Function
print('\nThe search Function')
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())


#Another Example
print('\nAnother Example')
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


#The split() Function
print('\nThe split Function')

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Anther Function
print('\nAnother Function')

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


#The sub() Function
print('\nThe sub Function')

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

#Another Example
print('\nAnother Example')

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)


#Match Object
print('\nMatch Object')
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object


#Another Example
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


#Another Example
print('\nAnother Example') 
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


#Another example print where match
print('\nAnother example print where match')
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())