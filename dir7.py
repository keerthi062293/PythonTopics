#Directories
#rmdir("delted directory name") is used to delete or remove dirctory form the current working directory.
#it delete's only empty directory.

import os
print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories
print()

print("Directories are: ",os.listdir()) #Directories are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'dir6.py', 'hello.txt', 'MDirectories', 'Newdirectory']
print()

os.rmdir("MDirectories")
os.rmdir("Newdirectory")

print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories

print("Directories are: ",os.listdir()) #Directories are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'dir6.py', 'hello.txt' ]

print()

print(os.getcwdb())