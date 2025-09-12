#Python Datetime

#A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.
print('\nPython Dates')
import datetime
x = datetime.datetime.now()
print(x)

print('\nDate Output')
print(x.year)
print(x.strftime("%A"))


#Creating Date Objects
print('\nCreating Date Objects')
x = datetime.datetime(2020, 5, 17)
print(x)

#The strftime() Method
print('\nThe strftime() Method')
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))