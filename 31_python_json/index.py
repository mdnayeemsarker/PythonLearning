#Python JSON

#JSON in Python
#Python has a built-in package called json, which can be used to work with JSON data.
print('\nJSON in Python')
import json

#Convert from JSON to Python
print('\nConvert from JSON to Python')
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])