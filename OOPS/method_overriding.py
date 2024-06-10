'''
Method overriding is an ability of any object-oriented programming language that allows a 
subclass or child class to provide a specific implementation of a method that is already 4
provided by one of its super-classes or parent classes. When a method in a subclass has the same name, 
same parameters or signature and same return type(or sub-type) as a method in its super-class, 
then the method in the subclass is said to override the method in the super-class.
'''

class Animal():
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dogs Bark")

class bird(Animal):
    def sound(self):
        print("Birds Sings")


a = bird()
a.sound()
