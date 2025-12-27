class Base1:
    def multiply(self,a,b):
        self.a = a
        self.b = b
        return self.a * self.b # ALT: reutrn a * b

class Base2(Base1):
    def add(self,a,b):
        return a + b

class Derived(Base2):
    def subtract(self,a,b):
        return a-b

o = Derived()
print(o.add(1,2))
print(o.subtract(5,3))
print(o.multiply(3,2))
    