# Python script to generate n Number of folders
# Author Sami
import os
n = int(input("Enter Number of Folders You Want: ")) 
i = 1
fname = str(input("Enter Folders Name/Leave it Blank: "))
ch = input("Do You Want to Change Path?(y/n)")
if ch == 'y':
	path = str(input("Enter New Path: "))
	os.chdir(path) # will change the current dir to 'Path' dir
try:
	while(n>0 and i<=n):
		nfname = fname + str(i) #ex: a + 1 = a1
		os.mkdir(nfname) # will creates folders in current dir
		i+=1
except:
	print("Exception Occured")
print (n, " Folder Created!")

