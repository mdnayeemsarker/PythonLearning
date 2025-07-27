#Python Operators

#Arithmetic operators
print("Arithmetic operators")

print(5+6) #Addition
print(15-6) #Subtraction
print(15*6) #Multiplication
print(15/6) #Division
print(15%6) #Modulus
print(2 ** 6) #Exponentiation
print(25 // 2) #Floor division = the floor division // rounds the result down to the nearest whole number

#Assignment Operators are used to assign values to variables:
print("\nAssignment Operators")

a = 25
b = 12

print(a)

c = 6
c += a
print(c)

c = 36
c -= a
print(c)

c = 3
c *= a
print(c)

c = 100
c /= a
print(c)

c = 160
c %= a
print(c)

c = 160
c //= a
print(c)

c = 6
c **= a
print(c)

c = 25
c &= a
print(c)

c = 250
c |= a
print(c)

c = 250
c ^= a
print(c)

c = 2
c >>= a
print(c)

c = 2
c <<= a
print(c)

print(c := a)


#Comparison Operators
print("\nComparison Operators")

i = 25
j = 22

print(i == j)
print(i != j)
print(i > j)
print(i < j)
print(i >= j)
print(i <= j)


#Logical Operators
print("\nLogical Operators")
print(i > j and i < j)
print(i < j and i > j)

print(i > j or i < j)
print(i < j or i > j)

print(not(i > j and i < j))
print(not(i < j and i > j))


#Identity Operators
print("\nIdentity Operators")

print(a is b)
print(a is not b)


#Membership Operators
print("\nMembership Operators")

print(a in ("25","26"))
print(a not in ("25", "27"))


#Bitwise Operators
print("\nBitwise Operators")

print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(6 << 3)
print(6 >> 3)


#Operator Precedence
print("\nOperator Precedence")
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3) # first + then - then +