#Python - Unpack Tuples 

#Unpacking a Tuple
print("\nUnpacking a Tuple")
mytuple = ("apple", "banana", "cherry")
print(mytuple)

(green, yellow, red) = mytuple

print(green)
print(yellow)
print(red)


#Using Asterisk*
print("\nUsing Asterisk*")
mytuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = mytuple

print(green)
print(yellow)
print(red)

#another way
(green, *tropic, red) = mytuple

print(green)
print(tropic)
print(red)