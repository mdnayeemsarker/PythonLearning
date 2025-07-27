# Python - Modify Strings

aboutMe = " my name is, md nayeem sarker "

#upper case
aboutMe2 = aboutMe.upper()
print(aboutMe.upper())

#lower case
print(aboutMe2.lower())

#remove whitespace
print(aboutMe.strip()) 

#Replace String
print(aboutMe.replace("md nayeem sarker", "MD NAYEEM SARKER"))

#Split String
varSplit = "name, age, phone, address, website"
print(varSplit.split())