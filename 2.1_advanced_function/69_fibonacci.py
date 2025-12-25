def fibo(n):
    # recursive function, fibo is called by itself
    print(f"calculating fibo {n}")
    return 1 if n < 3 else fibo(n-1)+fibo(n-2)

print(fibo(6))
print('after printing fibo 6.....')
print(fibo(7))
