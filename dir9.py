#Directiories
#os.makedirs() is used to create the directory recursively,that means while creating the leaf dirctory if any intermediate dirctories is missing.os.makedirs() will create them all.
#os.makedirs(path, mode,exist_ok=true/false) has 3 paramenters.
#path is address which where we want to create the directory. 
#mode is optional,it returns the interger value.
#exist_ok=false it defaulty take the false,if the directory doesn't exist it create the new directory.
#exist_ok=true menas if directory is alredy exist it retruns the error.

import os
import time

print(os.getcwd())
print()

print("Directories are:", os.listdir())
print()

os.makedirs("newdirectory",exist_ok=True)
print(os.getcwd())

print("Directoires are: ",os.listdir())