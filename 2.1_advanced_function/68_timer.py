def logger(fn):
    from functools import wraps
    from datetime import datetime,timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print("{0} was called {1}, recent data: {2}".format(
            fn.__name__,dt, result
        ))
        return result
    
    return inner

def timer(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        # to keep track of starting and ending time
        start_time = perf_counter()
        result = fn(*args, **kwargs)
        end_time = perf_counter()
        time_taken = end_time-start_time

        #diplay time taken by function
        print("{0} ran for {1:.6f}".format(fn.__name__,time_taken))
        return result # result stores the fn's returned value
    return inner

@logger #first (closest to fn)
@timer # second 
def factorial(n):
    from operator import mul
    from functools import reduce
    return reduce(mul,range(1,n+1))

print(factorial(10))
