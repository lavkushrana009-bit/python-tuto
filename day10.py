# OOPS 
#class and object in python
#Class are the blueprint for creating objects
#creating class



class Student:
    name ="lavkush kumar"
    roll_no=21
    course="Maths & computing"



# creating object (instance)
s1=Student()
print(s1)
print(s1.name)
print(s1.roll_no)
print(s1.course)

#__init__ Function  (Constructor)
# All classes have a function __init__() ,which is always executed when the class is being initialed.

#creating class

class Student:
    #defining constructor
    def __init__(self):
        pass
#parameterized constructor
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding student details")

#creating object
s1=Student("lav",40)
print(s1.name,s1.marks)

s2=Student("rana",41)
print(s2.name,s2.marks)


""" The self parameter is a reference to the current instance of the class,
 and is used to access variables that belong to the class  """
