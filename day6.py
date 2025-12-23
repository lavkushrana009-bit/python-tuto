#loop are used to repeat inteructions
#There are two types of loops in python
#1.for loop
#2.while loop

#while loop
i=1
while i<=5:
    print(i)
    i=i+1  



# break and contionus ststement
# break-stops the loop
# continue-skips the current iteration and moves to the next iteration   

  
#break statement
i=1
while i<=5:
    print(i)
    if (i==3):
        break
    i=i+1    

#continue statement
i=1
while i<=5:
    if (i==3):
        i=i+1 
        continue #skip
    print(i)
    i=i+1 



#for loop
for i in range(1,6):
    print(i)


#range() function returns a sequence of numbers starting from 0 by default,
# and increments by 1 (by default), and stops before a specified number.

#range(stop)
for i in range(6):
    print(i)

#range(start,stop)
for i in range(1,11):
    print(i)

#range(start,stop,step)
for i in range(1,11,2):
    print(i)  

#pass statement
#pass statement is used to avoid getting error when a statement is required syntactically
for i in range(1,6):
    pass
    print(i)

