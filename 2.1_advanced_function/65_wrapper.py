# docstring (document string) 
# """"docstring""""

# a built-in Python library designed
#  for higher-order functions
from functools import wraps

# decorator
def log(fn):
    @wraps(fn) #to keep fn's docstring
    def with_log(*args, **kwargs):
        print(fn.__name__ +  " was called")
        return fn(*args, **kwargs) #call myfun
    return with_log

@log
def myfun(x):
    """operations like arithmetic"""
    return x*3

@log
def myfun2(x):
    """Docstring of myfun2"""
    return x*2

myfun(5)
print(myfun.__name__) # inner fn of decorator
print(myfun.__doc__)

myfun2(10)
print(myfun2.__name__)
print(myfun2.__doc__)