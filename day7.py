#functions in python
#block of statements that perform a special task
#defined using def keyword

def sum(a,b):
    c=a+b
    return c
print("The sum is:",sum(5,10))

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


