#Directories
#os.path.isfile(existed file name) it return the true/flase.
#if it return 'true',the file is exist in current working directory.
#if it return 'flase', the file is doesn't exist in current working directory.
# os.path.isfile(path address) it take path address to find a directory.
#os.path.isfile() find only files(like txt,py etc).

import os
import time

print(os.path.isfile("dir1")) #false
print(os.path.isfile("dir1.py"))#true
print(os.path.isfile("dummy")) #false

print()

time.sleep(2)

print(os.path.isfile("C:\\Users\\keert\\onedrive\\desktop\\pp\\directories\\dir1.py")) #true