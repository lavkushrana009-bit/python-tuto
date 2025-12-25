#recursion 

def factorial(n):#parameters
    if (n==0 or n==1):#base case
        return 1
    else:
        return n*factorial(n-1)#recursive case
    
num=int(input("Enter a number to find its factorial:"))
print("Factorial of",num,"is:",factorial(num))


#iterative approach
def factorial_iterative(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result   
print("Factorial of",num,"using iterative approach is:",factorial_iterative(num))   

#practice problem
#write a recursive function to calculate the sum of first  n natural numbers.
def sum_nut(n):
    if (n==1):
        return 1
    else:
        return n+sum_nut(n-1)

n=int(input("Enter a number to find the sum of first n natural numbers:"))
print("Sum of first",n,"natural numbers is:",sum_nut(n))


#write a recursive function to print all elements in a list
#use list and index as parameters

def print_lst_elements(lst,index):
    if len(lst)<=index:
        return
    print(lst[index])
    print_lst_elements(lst,index+1)
my_list=[10,20,30,40,50]
print("Elements in the list are:")
print_lst_elements(my_list,0)





 