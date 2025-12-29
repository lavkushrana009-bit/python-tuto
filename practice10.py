#Exercise
#create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
  #   we are learning file I/O
   #  using Java.
   #  I like programming in Java 

with open("practice.txt","w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning file I/O\n")
    f.write("using Java.\n")
    f.write("I like programming in Java\n")


#WAF tat replace all occurrences of "Java" with "Python" in the file "practice.txt"
def replace_java_with_python(filename):
    with open(filename,"r") as f:# read mode
        data=f.read()# read all data
    data=data.replace("Java","Python")# replace all occurrences
    print("Modified Data:\n",data)# print modified data

    with open(filename,"w") as f:# write mode
        f.write(data)# write modified data back to file

replace_java_with_python("practice.txt")# call the function


#Search if the word "learning" exists in the file "practice.txt"
with open("practice.txt","r") as f:
     data=f.read()
     if "learning" in data:
        print("The word \"learning\" exists in the file.")
     else:
        print("The word \"learning\" does not exist in the file.")


#or
with open("practice.txt","r") as f:
     data=f.read()
     if (data.find("learning")!=-1):
        print("The word \"learning\" exists in the file.")
     else:
        print("The word \"learning\" does not exist in the file.")


#WAF a file in which line of the file does the world "learning" exists.
#print -1 if word does not exist in the file.

def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if word in data:
                print(f"The word \"{word}\" exists in line number {line_no}.")
                data=False
            else:
                print("-1")

            line_no+=1  
check_for_line()        

#from a file containing numbers separated by comma,print the count of even numbers
with open("pra.txt","r") as f:
    data=f.read()
    print("Data in file:",data)
    numbers=data.split(",")# split by comma
    print("Numbers List:",numbers)
    even_count=0
    for num in numbers:
        if int(num)%2==0:
            even_count+=1
    print("Count of even numbers:",even_count)
