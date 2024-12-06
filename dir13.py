#Directories
#os.path.isdir(path address) it return the boolean value,it used to check the wheather a given path exist and points to directory in the file system.
#it return ture,if the path is exist and refers to directory in the file system otherwise it returns flase. 
#it take only path address doesn't take the directoires/files even though its exists
import os
import time

x=os.getcwd()
print(os.path.isdir("./loops")) #false
print(os.path.isdir("./CDirectories")) #False
print(os.path.isdir("C:\\Users\\keert\\onedrive\\desktop")) #True
print(os.path.isdir(x)) #True
