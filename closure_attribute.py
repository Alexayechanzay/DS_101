#closure usage 
def myFun(n):
    def adding(data):
        return n + data
    return adding

ten_add = myFun(10)
two_add = myFun(2)

print(ten_add.__closure__) #if fun-obj is closure, the cell obj is returned as tuple
print(ten_add.__closure__[0].cell_contents)
print(two_add.__closure__[0].cell_contents)

#non-closure fun
def test():
    print("Hellow")
print(test.__closure__) # None (cuz not closure)