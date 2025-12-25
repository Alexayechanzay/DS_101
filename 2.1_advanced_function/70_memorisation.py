def memorize(fibo):
    from functools import wraps
    cache = {1:1, 2:1}

    @wraps(fibo)
    def inner(n):
        if n not in cache:
            # add new n's cache data into cache
            cache[n] = fibo(n)
        return cache[n]
    return inner


@memorize
def fibo(n):
    # recursive function, fibo is called by itself
    print(f"calculating fibo {n}")
    return 1 if n < 3 else fibo(n-1)+fibo(n-2)

print(fibo(6))

