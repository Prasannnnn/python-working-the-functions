# def power(a,b):
#     if b!=0:
#         return a*power(a,b-1)
#     else:
#         return 1
# a=float(input())
# b=float(input())
# print(a,"to the power",b,"is", power(a,b))


########Recursion Methods######################

# def great():
#     print("Hello World")
#     great()

# great()


##############Factorial#########################

# def fact(n):
#     if n == 0 :
#         return 1
#     else:
#         return n*fact(n-1)
# x = fact(5)
# print(x)


###########Add Two Numbers################
# def add(a,b):
#     if b == 0:
#         return a
#     else:
#         return add(a+1,b-1)
    
# a=int(input("Enter the number: "))
# b=int(input("Enter the b value: "))
# x = add(a,b)
# print(x)

###########product two numbers#############
# def pro(x,y):
#     if y == 0:
#         return 0
#     elif  y<0:
#         return -pro(x,-y)
#     else:
#         return x+pro(x,y-1)
    
# x = pro(5,-3)
# print(x)
    
############length of string###################
# def length(str):
#     if str == "":
#         return 0
#     return 1 + length(str[1:])
# str = "prasanna"
# print("the length of ", str)


#############tri recursion######################
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)



#####################lambda###########
#lambda arguments:expression
# x = lambda a : a + 10
# print(x(5))

#Multiply argument a with argument b and return the result

# x = lambda a, b : a * b
# print(x(5,6))


# x= lambda a,b,c : a + b + c
# print(x(5,6,2))

#prime number
# def is_prime(n,i=2):
#     if n <=2:
#         return n==2
#     if n % i == 0:
#         return False
#     if i*i>n:
#         return True
    
#     return is_prime(n,i+1)
# n=float(input())
# print(is_prime(n))


#Class and Objects
class x:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age = age
#The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned
    def __str__(self) -> str:
        return f"{self.name}({self.age})"


y = x("Hema",24)
print(y)