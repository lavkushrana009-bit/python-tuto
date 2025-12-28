# file I/O in python
#python can be used to perform operation on a file(read & write)
#Type of  files
# text files -> .txt, .py, .c, .cpp
# binary files -> .jpg, .png, .pdf
# opening a file

f=open("demo.txt","r")  # r-> read mode, w-> write mode, a-> append mode
data=f.read()
print(data)
print(type(data))
f.close()


#reading a file 
f=open("demo.txt","r")
data=f.readline()  # reads first line
print(data)
data=f.read(5)  # reads first 5 characters
print(data) 
f.close()

# 'w' mode -> write mode ,but truncates the file(overwrite)
f=open("demo1.txt","w")
f.write("Hello World\n")
f.write("Welcome to Python file handling\n")
print("Data written successfully")
f.close()

#'x' mode -> create a new file and open it for writing
f=open("demo2.txt","x")
f.write("This is a new file created using x mode\n")
f.close()

 # 'a' mode -> append mode, write data at the end of the file
f=open("demo.txt","a")
f.write("I am aspirants of Dat science\n")
f.close()
 # 'b' mode -> binary mode
f=open("demo.txt","rb")
data=f.read()
print(data)
f.close()


 # '+' mode -> read and write mode
f=open("demo.txt","r+")
data=f.read()
print(data)
f.write("This is added using r+ mode\n")
f.close()

 # 't' mode -> text mode(default mode)
f=open("demo.txt","rt")
data=f.read()
print(data)
f.close()

    # 'wb+' mode -> write and read in binary mode   
    
f=open("demo.txt","r+")
data=f.write("RANA")
f.close()
    # 'rb+' mode -> read and write in binary mode
f=open("demo.txt","r+")
data=f.write("RANA")
f.close()

    # 'r+' mode -> read and write mode
f=open("demo.txt","r+")
data=f.write("RANA")
print(f.read())
f.close()

    # 'w+' mode -> write and read mode
f=open("demo.txt","w+")
print(f.read())
data=f.write("lavkush")
f.close()
#with syntax
with open("demo.txt","w") as f:
    data=f.write("new data")

with open("demo.txt","w") as f:
    data=f.write("new data")

 #deleting a file 
#using the os module
"""module (like a code library) is a file written by another programer that
generally has a function we can use"""
import os
os.remove("lol.txt")