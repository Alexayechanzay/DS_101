def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
print(double(10)) # 20

triple = multiplier(3)
print(triple(10)) # 30