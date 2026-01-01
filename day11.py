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
        