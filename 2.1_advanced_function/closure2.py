#closure usage 
def myFun(n):
    def adding(data):
        return n + data
    return adding

two_minus = myFun(-2) # always subtracts 10 from data
ten_add = myFun(10)
print(ten_add(1))
print(two_minus(100))

print(two_minus(ten_add(100)))