#Directories
#os.makedirs() is used to create the directory recursively,that means while creating the leaf dirctory if any intermediate dirctories is missing.os.makedirs() will create them all.
#os.makedirs(path, mode,exist_ok=true/false) has 3 paramenters.
#path is address which where we want to create the directory. 
#mode is optional,it returns the interger value.
#exist_ok=false it defaulty take the false,if the directory doesn't exist it create the new directory.
#exist_ok=true menas if directory is alredy exist it retruns the error.

import os

dir1="keerthi2"
dir2="C:\\Users\\keert\\onedrive\\desktop\\pp\\Dummy1\\Dummy2"

path=os.path.join(dir2,dir1)
#here we crateing the 'keerthi2' directory in 'dummy2' but here in 'pp' directory the 'dummy' and 'dummy2' directories are doesn't exist perious so by using os.makedirs() method we are create the 'keerthi2' in 'dummy2' directory
#if exist_ok=True it returns the error because the 'keerthi2' directory is already exist.
os.makedirs(path)
print("Directory Created",dir1) #FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:\\Users\\keert\\onedrive\\desktop\\pp\\Dummy1\\Dummy2\\keerthi2'
print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories