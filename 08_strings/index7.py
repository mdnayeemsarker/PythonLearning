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
print("\nisalnum")
print(myName.isalnum())
print("125478".isalnum())

#isalpha = Returns True if all characters in the string are in the alphabet
myName1 = "mynameisMdNayeemSarker"
print("\nisalpha")
print("125478".isalpha())
print(myName1.isalpha())

#isascii = Returns True if all characters in the string are ascii characters
print("\nisascii")
print("125478".isascii())
print(myName1.isascii())

#isdecimal = Returns True if all characters in the string are decimals
print("\nisdecimal")
print("125478".isdecimal())
print(myName1.isdecimal())

#isdigit = Returns True if all characters in the string are digits
print("\nisdigit")
print("125478".isdigit())
print(myName1.isdigit())

#isidentifier = Returns True if the string is an identifier
print("\nisidentifier")
print("125478".isidentifier())
print(myName1.isidentifier())

#islower = Returns True if all characters in the string are lower case
print("\nislower")
print("asjdhfbas".islower())
print(myName1.islower())

#isnumeric = Returns True if all characters in the string are numeric
print("\nisnumeric")
print("145554".isnumeric())
print(myName1.isnumeric())

#isprintable = 	Returns True if all characters in the string are printable
print("\nisprintable")
print("Hello!\nAre you #1?".isprintable())
print(myName1.isprintable())

#isspace = 	Returns True if all characters in the string are whitespaces
print("\nisspace")
print("   ".isspace())
print(myName1.isspace())

#istitle = 	Returns True if the string follows the rules of a title
print("\nistitle")
print("Hello, And Welcome To My World!".istitle())
print(myName1.istitle())

#isupper = 	Returns True if all characters in the string are upper case
print("\nisupper")
print("MD NAYEEM SARKER".isupper())
print(myName1.isupper())

#join = Joins the elements of an iterable to the end of the string
print("\nisupper")
x = "#".join(("MD ", "NAYEEM ", "SARKER"))
print(x)

#ljust = Returns a left justified version of the string
print("\nljust")
print(myName1.ljust(50), "is my favorite fruit.")

#lower = Converts a string into lower case
print("\nljust")
print(myName1)
print(myName1.lower())

#lstrip = Returns a left trim version of the string
print("\nlstrip")
txt = "           banana         "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

#maketrans = Returns a translation table to be used in translations
print("\nmaketrans")
mynameTable = str.maketrans("S", "M")
print(myName.translate(mynameTable))

#partition = Returns a tuple where the string is parted into three parts
print("\npartition")
print(myName.partition("NAYEEM"))

#replace = Returns a string where a specified value is replaced with a specified value
print("\nreplace")
print(myName.replace("NAYEEM", "asha"))

#rfind = Searches the string for a specified value and returns the last position of where it was found
print("\nrfind")
print(myName.rfind("NAYEEM"))

#rindex = Searches the string for a specified value and returns the last position of where it was found
print("\nrindex")
print(myName.rindex("NAYEEM"))

#rjust = Returns a right justified version of the string
print("\nrjust")
print(myName.rjust(50), "this is rjust")

#rpartition = Returns a tuple where the string is parted into three parts
print("\nrpartition")
print(myName.rpartition("NAYEEM"))

#rsplit = Splits the string at the specified separator, and returns a list
print("\nrsplit")
myName2 = "apple, banana, cherry"
print(myName2.rsplit(", " ))

#rstrip = Returns a right trim version of the string
print("\nrstrip")
txt = "       banana                          "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

#split = Splits the string at the specified separator, and returns a list
print("\nsplit")
myName3 = "apple, banana, cherry"
print(myName3.split())

#splitlines = Splits the string at line breaks and returns a list
print("\nsplitlines")
myName3 = "Thank you for the music\nWelcome to the jungle"
print(myName3.splitlines())

#startswith = Returns true if the string starts with the specified value
print("\nstartswith")
myName3 = "Thank you for the music\nWelcome to the jungle"
print(myName3.startswith("Thank"))
print(myName3.startswith("You"))

#strip = Returns a trimmed version of the string
print("\nstrip")
txt = "     banana                 "
x = txt.strip()
print("of all fruits", x, "is my favorite")

#swapcase = Swaps cases, lower case becomes upper case and vice versa
print("\nswapcase")
print(myName3.swapcase())

#title = Converts the first character of each word to upper case
print("\ntitle")
print(myName3.title())

#translate = Returns a translated string
print("\ntranslate")
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#upper = Converts a string into upper case
print("\nupper")
print(myName1.upper())

#zfill = 	Fills the string with a specified number of 0 values at the beginning
print("\nzfill")
print("40".zfill(5))