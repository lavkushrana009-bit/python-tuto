#Create student class that takes name and marks of  subjects as arguments in constructor.
#Then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum +=val 
        print("hi",self.name,"your avg score is ",sum/3)

s1= Student("lav",[36,43,39])
s1.get_avg()

s1.name="lavkush rana"
s1.get_avg()



#CREATE ACCOUNT CLASS WITH 2 ATTRIBUTES- balance & account no.
#CREATE METHODS FOR DEBIT, CREDIT & PRINTING THE BALANCE

class Account:
    def __init__ (self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
        #debit method
    def debit(self,amount):
        self.balance -= amount
        print("debited",amount)
        print("total balance",self.get_balance())
        #credit method
    def credit(self,amount):
        self.balance += amount
        print("credit",amount)
        print("total balance",self.get_balance())


    def get_balance(self):
         return self.balance



s1=Account(63500,66768)  

print(s1.balance)
print(s1.account_no)

s2=Account(500,4534567)
s2.debit(2000)
s2.credit(3000)

s2.credit(7000)
s2.debit(2000)

