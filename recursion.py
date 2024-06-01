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
def length(str):
    if str == "":
        return 0
    return 1 + length(str[1:])
str = "prasanna"
print("the length of ", str)