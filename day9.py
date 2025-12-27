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
f=open("demo.txt","x")
f.write("This is a new file created using x mode\n")
f.close()

