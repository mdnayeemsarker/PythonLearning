#Python While Loops

#Python has two primitive loop commands:
  # while loops
  # for loops

#The while Loop
print("\nThe while Loop")
i = 1
while i < 6:
  print(i)
  i += 1


#The break Statement
print("\nThe break Statement")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  
#The continue Statement
print("\nThe continue Statement")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#The else Statement
print("\nThe else Statement")
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")