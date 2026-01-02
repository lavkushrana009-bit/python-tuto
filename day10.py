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


#class & instance attributes
#class.attr
#obj.attr

class Student:
    college_name="Mnnit Allahbad"
    name="anonymous" #class attr

    def __init__(self,name ,marks):
        self.name=name#obj attr > class attr   (   precedence  )
        self.marks=marks
        print("adding new student in database")


s1=Student("amar",55)
print(s1.name,s1.marks)

s2=Student("lav",43)
print(s2.name,s2.marks)

print(Student.college_name)

print(s1.college_name)

print(s2.college_name)
print(s1.name)

#method
#method are functions that belong to objects.
class Student:
    college_name="Mnnit Allahbad"
    name="anonymous" #class attr

    def __init__(self,name ,marks):
        self.name=name#obj attr > class attr   (   precedence  )
        self.marks=marks

    def welcome(self):
        print("welcome student",self.name)

    def get_marks(self):
        return self.marks


s1=Student("lav",43)
s1.welcome()
print(s1.get_marks())



#Static  Methods 
#Methods that don't use the self parameter(work at class level)
class Student:
    @staticmethod #decorator
    def collge():
        print("MNNIT")

# Decorators allow us to wrap another function in order to
# extend the behaviour of the wrapped function,without permanently modifying it





#Important

#Abstraction
#Hiding the implementations details of class and only showing
#the essential features to the user

class Car:
    def __inti__(self):
        self.acc=False
        self.brk=False
        self.clutch=True

    def start(self):

        self.clutch=True
        self.acc=True
        print("car started..")

car1=Car()
car1.start()


#Encapsulation

#Wrapping data and functions into a single units(object).
  