def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count # to make a ref to outer var count
        count +=1

        #count the number of time program works
        print(f'function {func.__name__} was called {count}') 
        return func(*args, **kwargs) # working function, 
        """returned none, that's why when decorator is printed out
        it returns none"""

    return inner

def add(a,b=0): # working function
    """addingg two values using decorator"""
    print(a+b) 
    # default return none;
    # if return (a+b) is used, we have to print the obj.

def sub(a,b=0):
    """substract two values using decorator"""
    print(a-b)

result = counter(add)
r2 = counter(sub)
result(10,20)
r2(10,20)
r2(10,9)
result(30,40)
result(50,50)

"""In Python, every single function returns something. 
If you don't write an explicit return statement, 
Python automatically adds an invisible one 
at the very end of your function: return None."""