class Parent: # base
    def __init__(self,age):
        self.__age = age

class Child(Parent):
    def setData(self,usr_input):
        self.__age = usr_input
        return self.__age

    def getData(self):
        return(self.__age)


c1 = Child(12)
print(c1.setData(100))
print(c1.__dict__)
print(c1.getData())