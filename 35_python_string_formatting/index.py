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