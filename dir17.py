#Directories

import os
print(os.getcwd()) #C:\Users\keert\OneDrive\Desktop\PP\Directories

os.chdir("C:\\Users\\keert\\OneDrive\\Desktop\\PP")
os.rmdir("C:\\Users\\keert\\OneDrive\\Desktop\\PP\\CDirectories")

print(os.path.exists("C:\\Users\\keert\\OneDrive\\Desktop\\PP\\CDirectories"))
#FileNotFoundError: [WinError 2] The system cannot find the file specified: 'C:\\Users\\keert\\OneDrive\\Desktop\\PP\\CDirectories' the directory already deleted.