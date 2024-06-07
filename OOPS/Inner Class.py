class Student:
    def __init__(self,name,roll) -> None:
        self.name = name
        self.roll = roll
        self.lap = self.Laptap()

    def show(self) -> str:
        print(f'{self.name} is roll no {self.roll}')
        self.lap.show()

    class Laptap:
        def __init__(self) -> None:
            self.brand = "Dell"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu,self.ram)
            

stu1 = Student("Naren",789)
stu2 = Student("Deva",456)

lap1 = Student.Laptap()
stu1.show()