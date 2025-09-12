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

#Convert from Python to JSON
print('\nConvert from Python to JSON')
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

#You can convert Python objects of the following types, into JSON strings
print('\nconvert Python objects of the following types')
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))