# global g
# g = 9.8
# def myFun(n):
#     # global g # disclaim g = 10 will be used as global var
#     # g =10
#     v = g ** n
#     return v

# print(myFun(2))
# print(f"Golobal g var: {g}")

# non-local var
def outFun():
    
    d = "Green"
    def innerFun():
        nonlocal d
        d = "Java"
        print("innerFun's d value:",d)
    innerFun()
    print("outerFun's d value:",d)

outFun()