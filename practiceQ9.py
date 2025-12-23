#Print number 1 to 100
i=1
while i<=100:
    print(i)
    i=i+1 

 #Print number 100 to 1
i=100
while i>=1:
    print(i)
    i=i-1

#print the multiplication table of number n
n=int(input("Enter a number to print its multiplication table: "))
i=1
while i<=10:
    print(n,"x",i,"=",n*i)
    i=i+1 


# Print the elements of the following list using while loop
num=[1,4,9,16,25,36,49,64,81,100]

idx=0
while idx<len(num):
    print(num[idx])
    idx=idx+1  
    

#Serch for a number x  in this tuple using while loop
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number to search in the tuple: "))
idx=0   
while idx<len(tup):
    if tup[idx]==x:
        print(x,"is found in the tuple at index",idx)
    idx=idx+1


#Print all odd numbers from 1 to 20 using while loop
i=1
while i<=20:
    if (i%2==0):
        i=i+1 
        continue #skip
    print(i)
    i=i+1
    



#Print all even numbers from 1 to 20 using while loop
i=1
while i<=20:
    if (i%2!=0):
        i=i+1 
        continue #skip
    print(i)
    i=i+1



# Print the elements of the following list using for loop
num=[1,4,9,16,25,36,49,64,81,100]

for i in num:
    print(i)

#Serch for a number x  in this tuple using for loop
tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter a number to search in the tuple: "))
for idx in range(len(tup)):
    if tup[idx]==x:
        print(x,"is found in the tuple at index",idx)   




# Practice Questions
# Print the number 1 to 10 using for loop
for i in range(1,11):
    print(i)

#print the number 10 to 1 using for loop
for i in range(10,0,-1):
    print(i)
# Print the multiplication table of a number n using for loop  
n=int(input("Enter a number to print its multiplication table: "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)   
  

# Practice Questions
#wap to find the sum of first n natural numbers using while loop
n=int(input("Enter a number: "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("Sum of first",n,"natural numbers is",sum)

#wap to find the factorial of first n numbers using for loop
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of",n,"is",fact)