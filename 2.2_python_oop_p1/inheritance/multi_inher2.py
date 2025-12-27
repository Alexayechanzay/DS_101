# Multiple inheritance 
#(Parents,adopted parents, relatives)'s attr & methods -> child class
class Parents: # base class
    def parent(self):
        print("This is from parent")

class Adopted_parents(Parents):# base class
    def adotped_parents(self):
        print("This is from adopted parents")

class Child(Adopted_parents):#derived class
    def child(self):
        print("This is from child!")

o = Child()
o.adotped_parents()
o.parent()
