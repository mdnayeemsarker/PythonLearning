#Python Delete File
#Delete a File

# To delete a file, you must import the OS module, and run its os.remove() function
print("Delete a File:")
import os
# os.remove("/home/abmn/Desktop/Python/41_file_delete/newfile.txt")

#Check if File exist
print("\nCheck if File exist:")
if os.path.exists("/home/abmn/Desktop/Python/41_file_delete/newfile.txt"):
  os.remove("/home/abmn/Desktop/Python/41_file_delete/newfile.txt")
else:
  print("The file does not exist")

#Delete Folder
print("\nDelete Folder:")
#To delete an entire folder, use the os.rmdir() method
# os.rmdir("/home/abmn/Desktop/Python/41_file_delete/myfolder") 
#Folder should be empty 
#Check if Folder exist
print("\nCheck if Folder exist:")
if os.path.exists("/home/abmn/Desktop/Python/41_file_delete/myfolder"):
  os.rmdir("/home/abmn/Desktop/Python/41_file_delete/myfolder")
else:
  print("The folder does not exist")