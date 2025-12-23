#arthmstic operators in Python  
a=4
b=2
print(a+b)
print(a-b)
print(a/b)#float division
print(a*b)  #multiplication
print(a%b) #remainder
print(a//b)#floor division
print(a**b)#power




#reational operators in python

print(a==b)#false     
print(a!=b)#true
print(a>b)  #true
print(a<b)#false
print(a>=b)#true
print(a<=b)     #false


#assignment operators in python 
c=5
c+=2  #c=c+2    
print(c)
c-=2  #c=c-2        
print(c)
c*=2  #c=c*2    
print(c)
c/=2  #c=c/2
print(c)
c%=2  #c=c%2            
print(c)
c//=2  #c=c//2    
print(c)    
c**=2  #c=c**2
print(c)


#logical operators in python
x=True
y=False 
print(x and y) #false
print(x or y)  #true    
print(not x)   #false
print(not y)   #true
print((a>b) and (a!=b)) #true
print((a<b) or (a==b))  #false
print(not(a==b))  #true
print((a>b) and (a==b)) #false
print((a<b) or (a!=b))  #true
print(not(a!=b))  #false


#conversion operators in 
"""conversion operators are used to convert one data type to another data type in  python automatically"""
p=10
q=20
print(float(p))  #10.0
print(int(q))    #20    
print(str(p))    #'10'
print(complex(q)) #20+0j    
print(bool(p))    #True
print(bool(0))    #False
print(complex(p,q)) #10+20j
print(str(q))     #'20' 

#typecasting in python
"""typecasting is the process of converting one data type into another data type in python manually"""
m="100" 
n=int(m)
print(n)      #100  
print(type(n)) #<class 'int'>
f=float(m)
print(f)       #100.0
print(type(f))  #<class 'float'>
s=str(n)
print(s)       #'100'   
print(type(s))  #<class 'str'>
b=bool(n)
print(b)       #True
print(type(b))  #<class 'bool'>
c=complex(n)       
print(c)       #(100+0j)


#input in python
name=input("enter your name:")
print("hello",name)
age=input("enter your age:")
print("your age is ",age)
marks=input("enter your marks:")
print("your marks are",marks)