class Myclass:
    def __init__(self,cat1,cat2): # special method
        self.cat1 = cat1
        self.cat2 = cat2
    
    def methodInfo(self): # normal method
        print(f"From method info: {self.cat1}: {self.cat2}")

o1 = Myclass("Apple","Orange")
print(f"Obj dat: {o1.cat1}, {o1.cat2}")
o1.methodInfo() # calling normal method