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