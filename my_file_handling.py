#f = open ("demofile.txt",'r')
#print(f.read())
#print(f.read(5))
#print(f.readline())
#print(f.close())

#f = open("demofile.txt",'a')
#print(f.write("There are more contents in the file now"))
#f.close()

#f = open("demofile.txt",'r')
#print(f.read())

#f =open("myfile.txt",'w')

import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("File doesn't exist")