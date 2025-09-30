#Python File Write
#Write to an Existing File

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
print("Write to an Existing File:")
f = open("/home/abmn/Desktop/Python/40_file_write_create/demofile.txt", "a")
f.write("\nNow the file has more content!")
f.close()
f = open("/home/abmn/Desktop/Python/40_file_write_create/demofile.txt", "r")
print(f.read())
f.close()

#Overwrite Existing Content
print("\nOverwrite Existing Content:")
f = open("/home/abmn/Desktop/Python/40_file_write_create/demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f = open("/home/abmn/Desktop/Python/40_file_write_create/demofile.txt", "r")
print(f.read())
f.close()

#Create a New File
print("\nCreate a New File:")
f = open("/home/abmn/Desktop/Python/40_file_write_create/newfile.txt", "x")
f = open("/home/abmn/Desktop/Python/40_file_write_create/newfile.txt", "w")
f.write("Hello! This is a new file.")
f.close()
f = open("/home/abmn/Desktop/Python/40_file_write_create/newfile.txt", "r")
print(f.read())
f.close()