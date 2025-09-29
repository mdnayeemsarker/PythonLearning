#Python String Formatting

#F-Strings
print("F-Strings")
txt = f"The price is 49 dollars"
print(txt)


#Placeholders and Modifiers
print("\nPlaceholders and Modifiers")
price = 59
txt = f"The price is {price} dollars"
print(txt)

#Placeholders and Modifiers another example
print("\nPlaceholders and Modifiers another example")
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


#Perform Operations in F-Strings
print("\nPerform Operations in F-Strings")
txt = f"The price is {59 * 0.8} dollars"
print(txt)

#Perform Operations in F-Strings another example
print("\nPerform Operations in F-Strings another example")
price = 59
tax = 0.2
txt = f"The price is {price * (price + tax)} dollars"
print(txt)

#You can perform if...else statements inside the placeholders:
print("\nYou can perform if...else statements inside the placeholders:")
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

#You can perform if...else statements inside the placeholders:
print("\nYou can perform if...else statements inside the placeholders:")
price = 69
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)


#Execute Functions in F-Strings
print("\nExecute Functions in F-Strings")
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

#Create a function that converts feet into meters
print("\nCreate a function that converts feet into meters")
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)


#More Modifiers
print("\nMore Modifiers")
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)


#String format() Method
print("\nString format() Method")
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

#Multiple Values
print("\nMultiple Values\n")
name = "John"
age = 30
txt = "My name is {} and I am {}"
print(txt.format(name, age))