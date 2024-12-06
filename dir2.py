#Directiories 
#chdir() is used to change the current working directory to new path directory.
#it returns the string value.
#here we use '\'(forward) or '/'(backward) to separate the path elements 
import os 
import time

l1=os.getcwd()
print(l1) #C:\Users\keert\onedrive\desktop\pp\directories

time.sleep(2)

os.chdir("C:\\Users\\keert\\OneDrive\\Desktop\\PP\\CDirectories")
l2=os.getcwd()
print(l2) #C:\Users\keert\OneDrive\Desktop\PP\CDirectories

time.sleep(2)

if(l1==l2):
    print("the dirctiory address didn't changed")
else:
    print("the directory address changed")

