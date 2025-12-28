#protected _, private __

class Parent: 
    def __init__(self,age):
        self._age = age #Warning! Do Not access it

class Sub(Parent):
    def getData(self):
        print(self._age)

o1 = Sub(18)
o1.getData()
o1._age = 17
print(o1._age)