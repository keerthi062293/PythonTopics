#Directories
#remove() is used to remove or delete the txt files from the current working directory.
#here we  are passing the txt file name.

import os
print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories
print()

print("Directories are: ",os.listdir()) #Directories are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'dir6.py', 'hello.txt', 'MDirectories', 'Newdirectory']
print()

os.remove('hello.txt')
print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories
print()

print("Directoires are: ",os.listdir()) #Directoires are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'dir6.py', 'MDirectories', 'Newdirectory']