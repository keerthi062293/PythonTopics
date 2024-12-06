#Directories
#Shutil is another module in python, rmtree() is used to in order to remove the non empty directory.
#we need to careful when using them it will delete the directory permanently from directory.
#it permanently delete the empty or non empty folders/directories from directory.

import os
import time

print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories
print()

print("Directories are: ",os.listdir()) #Directories are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'dir6.py', 'dir7.py', 'dir8.py', 'Dummy', 'Dummy2']
print()


import shutil
shutil.rmtree("Dummy")
shutil.rmtree("Dummy2")
print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories

print("Directiories are: ",os.listdir()) #Directiories are:  ['dir1.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'dir6.py', 'dir7.py', 'dir8.py']