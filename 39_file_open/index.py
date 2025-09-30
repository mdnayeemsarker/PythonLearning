#Python File Open

#File Handling
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

#Syntax 
#Open a File on the Server
print("Opening a file:")
# f = open("demofile.txt", "r")
# print(f.read())

#Open a File from local computer
print("\nOpening a file from local computer:")
f = open("/home/abmn/Desktop/Python/39_file_open/demofile.txt", "r")
print(f.read())

#Using the with statement
print("\nUsing the with statement:")
with open("/home/abmn/Desktop/Python/39_file_open/demofile.txt") as f:
  print(f.read())

#Close Files
print("\nClose Files:")
f = open("/home/abmn/Desktop/Python/39_file_open/demofile.txt")
print(f.readline())
f.close()

#Read Only Parts of the File
print("\nRead Only Parts of the File:")
f = open("/home/abmn/Desktop/Python/39_file_open/demofile.txt", "r")
print(f.read(5))
print(f.read(8))
f.close()