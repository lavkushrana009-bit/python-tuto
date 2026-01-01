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