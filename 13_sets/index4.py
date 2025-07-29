#Python - Remove Set Items 

#Remove Item
print("\nRemove Item")

myset = {"apple", "banana", "cherry"}
myset.add("orange")
print(myset)
myset.remove("banana") #it remove easily if the item is exist
print(myset)
# myset.remove("remove") #it will gettign issue
print(myset)


#discard
print("\nRemove Item by discard")
myset.discard("remove") #it not getting any error if item not exist
print(myset)


#pop
print("\nRemove Item by pop")
myset.pop() #it not remove random item
print(myset)


#clear
print("\nRemove Item by clear")
newset = {"apple", "banana", "cherry"}
newset.clear() #it clear the set
print(newset)


#The del keyword will delete the set completely:
print("\ndel the set by using keyword")
del myset
print(myset)