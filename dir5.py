#Directories 
#rename("old name","new name") method is used to rename the directory or file. 

import os
print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories
print()

print("Directories are: ",os.listdir()) #Directories are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'MDirectories']
print()

os.rename("MDirectories","Newdirectory")
print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories
print()

print("Directories are: ",os.listdir()) #Directories are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'Newdirectory']
