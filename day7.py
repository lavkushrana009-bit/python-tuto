#functions in python
#block of statements that perform a special task
#defined using def keyword
# repeat (redundant) code
# improve code readability

# def fun_name(par1,par2):#function definition
    #function body (some works)
    # return  #optional

# fun_name(arg1,arg2)#function call
 
def sum(a,b):#parameters
    c=a+b
    return c
print("The sum is:",sum(5,10))#arguments

def greet(name):
    print("Hello",name) 

greet("Alice")
greet("Bob")
greet("Charlie")
greet("Diana")
greet("Eve")


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("Factorial of 5 is:",factorial(5))
print("Factorial of 7 is:",factorial(7)) 


def is_even(num):
    if num%2==0:
        return True
    else:
        return False
    

print("Is 4 even?",is_even(4))
print("Is 7 even?",is_even(7))

#average of 3 numbers

def avg(a,b,c):
    return (a+b+c)/3

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))    
c=int(input("Enter third number:"))
print("Average of given numbers is:",avg(a,b,c))


#type of functions
#1. built-in functions
#print()
# len()
# type()
# range()

#2. user-defined functions

#waf print length of a list(list is the parameter) using function
cites=["New Delhi","Lucknow","Mumbai","pune","Chennai"]
def str_len(cites):
    print("Length of the string is:",len(cites)) 


#waf to print the elements of list in single line.(list is parameter
def print_list(cites):
    for city in cites:
        print(city,end=" ")


#waf to convert USD to INR(usd is parameter)
def usd_to_inr(usd):
    inr=usd*82.74
    return inr  
usd=float(input("Enter amount in USD:"))
print("Amount in INR is:",usd_to_inr(usd))  
