# lru_cache = least recently used cache (built-in decorator in funtool)
from functools import lru_cache

@lru_cache(maxsize=3) # None = unlimited 
def fib(n):
    print(f"calculating fib {n} ")
    return 1 if n < 3 else fib(n-1)+fib(n-2)

print(fib(5))
print(fib(2))