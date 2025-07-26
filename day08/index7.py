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