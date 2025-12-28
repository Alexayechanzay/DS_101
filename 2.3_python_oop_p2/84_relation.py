#issubclass(child, parent)#is child sub class of parent class?
#isinstance(obj, class)#is obj an inst of particular class?

class Parent:
    pass

class Child(Parent):
    pass

print(issubclass(Child, Parent))

p1 = Parent()
print(isinstance(p1, Parent))

c1 = Child()
print(isinstance(c1,Parent)) 