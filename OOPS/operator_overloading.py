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