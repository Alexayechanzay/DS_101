from myModule import fibo,listFibo
# ALT: import myModule

fibo(10)
print("\nFibonacci in list format")
print(listFibo(100))

del globals()["myModule"] # delete ["Module name"]

# fibo(4) #KeyError