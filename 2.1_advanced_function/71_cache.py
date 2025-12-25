def memorize(fibo):
    from functools import wraps
    cache = dict()

    @wraps(fibo)
    def inner(n):
        if n not in cache:
            # add new n's cache data into cache
            cache[n] = fibo(n)
        return cache[n]
    return inner

@memorize
def facto(n):
    print(f"Calculating factorial {n} !")
    return 1 if n < 2 else n*facto(n-1)

print(facto(5))
print("After 5 factorila")
print(facto(10))