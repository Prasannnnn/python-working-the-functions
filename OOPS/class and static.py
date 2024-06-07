'''
class Instance methods and class methods
'''

class Student:
    
    school = "St.paul"

    def __init__(self,m1,m2,m3) -> None:
        self.maths=m1
        self.science=m2
        self.social=m3

    def avg(self):
        return (self.maths+self.science+self.social)/3
    
    def get(self):
        return self.maths
    
    def set(self):
        self.maths = 80

    @classmethod
    def info(cls):
        return cls.school
    
    @staticmethod
    def infor():
        print("the statement is printing")

stu = Student(98,78,89)
mah = Student(89,54,64)


'''
Accessor only fetch the variables
Mutators only modify the variables
'''
print(stu.avg())
print(mah.avg())

print(stu.set())
print(stu.maths)

print(Student.info())
print(Student.infor())