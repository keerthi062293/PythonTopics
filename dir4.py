#Directories
#mkdir() is ued to create the new directory in current working directory.

import os
import time

print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories
print()

print("Directiories are: ",os.listdir()) #Directiories are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py']
print()

os.mkdir("MDirectories")
os.mkdir("hello.txt")
print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories
print()

print("Directories are: ",os.listdir()) #Directories are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py', 'MDirectories']