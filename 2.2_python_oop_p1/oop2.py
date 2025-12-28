class Myclass:
    def myMethod(self): #normal method
        self.x =10
        self.y =20

obj1 = Myclass()
obj2 = Myclass()

obj1.myMethod() #switch on button to activate normal method
print(obj1.x, obj1.y) # here: obj -> self

obj2.myMethod()
print(obj2.x, obj2.y)