def myfunc(x,y): #original code
    return(x/y)

# decorator 
def working(func):
    def inner(x,y):
        #swap if x < y, otherwise, use default
        if x<y:
            x,y=y,x
        return func(x,y)
    return inner

div = working(myfunc)
print(div(20,4)) # must have same output
print(div(4,20)) # smae output