def myFun():
    data = "i belong to myFun"
    def inner():
        print(data)
    return inner

obj1 = myFun()
del myFun

obj1()
# closure func req 
# 1.Nested fun , 
# 2.inner fun must call outer fun's data, 
# 3.when outer fun is called, inner fun must be returned. 