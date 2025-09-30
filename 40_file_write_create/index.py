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