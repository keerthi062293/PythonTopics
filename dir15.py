#Directories

import os 
import time 

if os.path.isdir("C:\\Users\\keert\\onedrive\\desktop\\pp\\directories"):
    os.chdir("C:\\Users\\keert\\onedrive\\desktop\\pp\\directories")
    print("Directories are: ", os.listdir())
    #Directories are: ['dir1.py', 'dir10.py', 'dir11.py', 'dir12.py', 'dir13.py', 'dir14.py', 'dir15.py', 'dir16.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'dir6.py', 'dir7.py', 'dir8.py', 'dir9.py', 'newdirectory']
    print()
    l1=os.listdir()
    time.sleep(3)
    for x in l1:
        if x=="dir16.py":
            os.remove(x)
            time.sleep(2)
            print()
    print("Directories are:", os.listdir())
    #Directories are: ['dir1.py', 'dir10.py', 'dir11.py', 'dir12.py', 'dir13.py', 'dir14.py', 'dir15.py', 'dir2.py', 'dir3.py', 'dir4.py', 'dir5.py', 'dir6.py', 'dir7.py', 'dir8.py', 'dir9.py', 'newdirectory']
            