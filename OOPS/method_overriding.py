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
