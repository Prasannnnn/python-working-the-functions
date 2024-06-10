'''
Operator Overloading means giving extended meaning beyond their predefined operational meaning. 
For example operator + is used to add two integers as well as join two strings and merge two lists. 
It is achievable because ‘+’ operator is overloaded by int class and str class. 
You might have noticed that the same built-in operator or function shows different behavior for 
objects of different classes, this is called Operator Overloading. 

'''

a = 56
b = 60

# print(a+b)

print(int.__add__(a,b))
print(int.__sub__(a,b))
print(int.__mul__(a,b))
print(int.__divmod__(a,b))
# print(int.__floor__(a,b))
print(int.__floordiv__(a,b))
print(int.__mod__(a,b))
print(int.__pow__(a,b))



'''
How Does the Operator Overloading Actually work?

Whenever you change the behavior of the existing operator through operator overloading, you have to 
redefine the special function that is invoked automatically when the operator is used with the objects. 

'''


class A:
    def __init__(self, a):
        self.a = a
 
    # adding two objects 
    def __add__(self, o):
        return self.a + o.a 
ob1 = A(1)
ob2 = A(2)
ob3 = A("MSD")
ob4 = A("Thala")
 
print(ob1 + ob2)
print(ob3 + ob4)
# Actual working when Binary Operator is used.
print(A.__add__(ob1 , ob2)) 
print(A.__add__(ob3,ob4)) 
#And can also be Understand as :
print(ob1.__add__(ob2))
print(ob3.__add__(ob4))


'''
Another Example:
'''

class complex:
    def __init__(self,a,b) -> None:
        self.a =a 
        self.b =b

    def __add__(self,others):
        return self.a +others.a , self.b + others.b

x = complex(5,6)
y = complex(6,8)
z = x + y
print(z)

'''
---> Overloading comparison operators in Python 
---> Overloading equality and less than operators: 



Operator	Magic Method
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
Comparison Operators:
Operator	Magic Method
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)
Assignment Operators:

Operator	Magic Method
-=	__isub__(self, other)
+=	__iadd__(self, other)
*=	__imul__(self, other)
/=	__idiv__(self, other)
//=	__ifloordiv__(self, other)
%=	__imod__(self, other)
**=	__ipow__(self, other)
>>=	__irshift__(self, other)
<<=	__ilshift__(self, other)
&=	__iand__(self, other)
|=	__ior__(self, other)
^=	__ixor__(self, other)
Unary Operators:

Operator	Magic Method
–	__neg__(self)
+	__pos__(self)
~	__invert__(self)
'''