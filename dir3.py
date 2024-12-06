#Directories
#listdir() is used to get the list of files and subdirectories are available in present working directory.
#it returns in list format.
#here we pass address as argument to get the list files and subdirectories.
#if we didn't pass any arugument it returns the list of files and subdirectories from the current working directiory.

import os
import time

print(os.getcwd()) #C:\Users\keert\onedrive\desktop\pp\directories

time.sleep(1)
print()

print("Directiories are: ",os.listdir()) #Directiories are:  ['dir1.py', 'dir2.py', 'dir3.py']

time.sleep(2)
print()

os.chdir("C:\\Users\\keert\\OneDrive\\Desktop\\PP\\CDirectories")
print(os.getcwd()) #C:\Users\keert\OneDrive\Desktop\PP\CDirectories

time.sleep(2)
print()

print("Directoires are: ",os.listdir()) #Directoires are:  []
print()

print("Directories from pp:",os.listdir("C:\\Users\\keert\\onedrive\\Desktop\\pp"))
#['1.py', '10.py', '11.py', '12.py', '13.py', '14.py', '15.py', '16.py', '17.py', '18.py', '19.py', '2.py', '20.py', '21.py', '22.py', '23.py', '24.py', '3.py', '4.py', '5.py', '6.py', '7.py', '8.py', '9.py', 'appendlist.py', 'basiclist.py', 'CDirectories', 'charvarargu.py', 'checkvaluelist.py', 'Dictionary', 'Directories', 'function.py', 'function2.py', 'indexforlistinlist.py', 'indexfunctioninlist.py', 'innercalling.py', 'insertlist.py', 'listindex.py', 'listinlist.py', 'listlength.py', 'listvalueupdate.py', 'oa.py', 'popfuninlist.py', 'python.py', 'removefunctioninlist.py', 'SET', 'set17.py', 'Untitled-1.py', 'varargu.py', 'za.py', 'zero argument.py']