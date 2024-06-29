def swap(func):

    def inner(a,b):
        if a < b:
            a,b = b,a 
        return func(a,b)
    return inner

@swap
def div(a,b):
    print(a/b)
div(4,16)