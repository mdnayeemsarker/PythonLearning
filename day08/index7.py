# Python - String Methods

myName = "my name is MD NAYEEM SARKER my my Ståle."

#capitalize = Converts the first character to upper case
print(myName.capitalize())

#casefold = Converts string into lower case
print(myName.casefold())

#center = Returns a centered string
tet = "SARKER"
x = tet.center(20)
print(x)

#count = Returns the number of times a specified value occurs in a string
print(myName.count("my"))

#encode = Returns an encoded version of the string
print(myName.encode())

#endswith = Returns true if the string ends with the specified value
print(myName.endswith("."))
print(myName.endswith("?"))

#expandtabs = Sets the tab size of the string
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

#find()	Searches the string for a specified value and returns the position of where it was found
print(myName.find("NAYEEM"))

#Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.5654))

#format_map = Formats specified values in a string
print(myName.format_map(1))

#index = look like find() Searches the string for a specified value and returns the position of where it was found
print(myName.index("NAYEEM"))

#isalnum = Returns True if all characters in the string are alphanumeric
print(myName.isalnum())
print("125478".isalnum())