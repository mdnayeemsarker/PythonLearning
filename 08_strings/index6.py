# Python - Escape Characters

#Single Quote
myName = "My name is MD NAYEEM SARKER, I\'m 130 years 'old'"
print(myName)

#Backslash
backslash = "This will insert one \\ (backslash)."
print(backslash)

#New Line
myName = "My name is MD NAYEEM SARKER, \nI\'m 130 years 'old'"
print(myName)

#Carriage Return
myName = "My name is MD NAYEEM SARKER, \rI\'m 130 years 'old'"
print(myName)

#Tab
myName = "My name is MD NAYEEM SARKER, \tI\'m 130 years 'old'"
print(myName)

#Backspace
myName = "My name is MD NAYEEM SARKER,\b \b I\'m 130 years 'old'"
print(myName)

#Octal value
#A backslash followed by three integers will result in a octal
txt = "\110\145\154\154\157"
print(txt)

#Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 