#string & conditional statements


str1="hello world"
str2='python programming'
str3="""welcome to coding"""

print(str1)
print(str2)
print(str3)

#scape sequences characters
str4="hello\tlavkush"
str5="hello\n lavkush"

print(str4)
print(str5)

#sting is  datatype that stores a sequence of characters
#basic opraters on string
#concatination

s1="hello"
s2="coders"
s3=s1+s2
print(s3)

#length of string  
#len() function
print(len(s3))
s4=s1+" "+s2
print(s4)
print(len(s4))


#indexing help to access individual characters in a string but we can't manupulate them
#indexing starts from 0 to n-1 where n is length of string

s="Lavkush Rana"
print(s[0]) #L
print(s[1]) #a
print(s[2]) #v

#slicing help to access asubstring from a string
#slicing syntax [start:end] end index is not included
print(s[0:4]) #Lavk
print(s[1:4]) #avk
print(s[8:13]) #Rana
print(s[8:len(s)]) #Rana
print(s[8:])#Rana
print(s[:3])

# negative indexing
# -1 refer to last character
s0="APPLE"
print(s0[-1]) #E
print(s0[-5:-1])

#string functions 
s5="hello world welcome to python programing"
print(s5.endswith("programing"))#return true if srting end with given substring else false

print(s5.capitalize()) #capitalize first character of string
# capitalize() doesn't change original string
print(s5)

print(s5.replace("python","C++")) #replace old substring with new substring

print(s5.find("world"))#return starting index of first occurence of substring else return -1

print(s5.count("w")) #return number of occurence of substring in string
print(s5.title()) #convert first character of each word to uppercase


# conditonal statements
#if-elif-else (SYNTAX)
""""
if (conditional):
stetement1
elif(conditional):
statement2
else:
statement3

  """

light=input("Enter the trafic light color:")

if (light=="green"):
    print("go ahead")#4 spaces before print caled indentation
elif(light=="yellow"):
    print("getready")
else:
    print("stop")


#nesting

age=int(input("Enter your age:"))
if(age>=18):
    if(age>=65):
        print("can't drive")
    else:
        print("can drive")
else:
    print("can't drive")