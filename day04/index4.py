#this is the variable Syntax
print("global variables")

globaleVar = "this is an globale variable"

def main():
    globaleVar = "functiona local varable"
    print(globaleVar)

main()

print(globaleVar)