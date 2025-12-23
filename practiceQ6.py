#Grade student baseon marks
marks=int(input("Enter the marks scoreed: "))
if (marks>=90):
    print("Grade A")
elif(marks>=80 and marks<90):
    print("Grade B ")
elif(marks>=70 and marks<80):
    print("Gade C")
else:
    print("Grade D")



#wap to check if a number enter by user is odd or even
num=int(input("Enter the integer:"))
if(num %2 == 0):
    print("number is even")
else:
    print("number is odd")


#wap t ofind the largest number amoung three numbers entered by user
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if(a>=b and a>= c):
    print(a," is largest")
elif(b>=a and b>=c):
        print(b," is largest")
else:
        print(c," is largest")


#Wap to check if a number is a multiple of 7
num=int(input("Enter the number:"))
if(num %7==0):
     print(num,"is multiple of 7")
else:
     print(num,"is not multiple of 7")