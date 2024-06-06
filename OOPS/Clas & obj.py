#this type only you have to create the class functions
#----> class is an blueprint
#----> object is an model

class Computer:#--------> Class function
    def config(self):
        print("i5","8GB","1TB")
#this is one of the methods
com = Computer()#----------> object

com.config()# ----------> object is calling the class function


'''
there is an another method
lets say one example class is a human and object is a name , so human body is the 
same of all the human persons in here human is a blueprint the same model of object 
is name I am giving the name all the persons
'''

class Human():
    def __init__(self,name,age,blood) -> None:
        self.name = name
        self.age = age
        self.blood = blood

    def __str__(self) -> str:
        return f"My name is {self.name} and the Age is {self.age} and my blood group is {self.blood}"

    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"
    

person1 = Human("Hema",24,"B+")
person2 = Human("Bhuvi",18,"B+")
person3 = Human("Praveen",22,"O+")
person4 = Human("Pranash",22,"A-")

print(person1)
print(person2)
print(person3)
print(person4)
