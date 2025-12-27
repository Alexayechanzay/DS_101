#4 built-in functions in class
#getattr(obj, attr_name) to acces the obj's attr
#setattr(obj, attr_name, value) to set the obj's attr to specified value
#delattr(obj, name)
#hasattr(obj, name)to check the presence of attr

class Student:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age

std = Student("Alex",369,17) # constructor 
print(std.__dict__)
print(getattr(std,"id"))

setattr(std,"id","ABC123")
print(getattr(std, "id"))

delattr(std, "age")
#print(std.__dict__)
print(hasattr(std, "age")) # False => std has no attr age