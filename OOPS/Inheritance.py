
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

#Multilevel inheritance
c=C()
c.britania()

#Multiple inheritance
d=C()
d.dinner()
d.britania()