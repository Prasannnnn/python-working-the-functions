
class A: # Super class
    def feature(self):
        print("feature is working")

    def major(self):
        print("major is working")
class B: # sub class
    def britania(self):
        print("50/50 is good")

    def parle(self):
        print("Krack Jack")

class C(B,A):
    def lunch(self):
        print("Variety rice")

    def dinner(self):
        print("Noodles")
#a = A()
#b = B()
# a.feature()
# a.major()
# b.britania()
# b.parle()
# b.feature()
# b.major()
#single level inheritance

# #Multilevel inheritance
# c=C()
# c.britania()

# #Multiple inheritance
# d=C()
# d.dinner()
# d.britania()

'''
sub class can access all the features of super class
but
super class cannot access any features of sub class
'''

'''
Constructor in Inheritace

Method Resolution Order
'''
# class A: # Super class
#     def __init__(self) -> None:
#         print("in A init")
#     def feature(self):
#         print("feature is working")

#     def major(self):
#         print("major is working")
# class B(A): # sub class
#     def __init__(self) -> None:
#         super().__init__()
#         print("in B init")

#     def britania(self):
#         print("50/50 is good")

#     def parle(self):
#         print("Krack Jack")



a = B()
'''
if you create object of sub class it will first try find init of sub class
if it is not found then it will call init of super class
'''


'''
when you create object of sub class it will call init of sub class first
if you have call super then it will first call init of super class then call init of sub class

'''


'''
Now If i Inherit both the classes A and B into C classes
'''


class A: # Super class
    def __init__(self) -> None:
        print("in A init")
    def feature(self):
        print("feature is working")

    def major(self):
        print("major is working")
class B: # sub class
    def __init__(self) -> None:
        print("in B init")

    def britania(self):
        print("50/50 is good")

    def parle(self):
        print("Krack Jack")

class C(B,A):

    def __init__(self) -> None:
        super().__init__()
        print("in C init")
    
    def lunch(self):
        print("Variety rice")

    def dinner(self):
        print("Noodles")

a = C()

a.britania()