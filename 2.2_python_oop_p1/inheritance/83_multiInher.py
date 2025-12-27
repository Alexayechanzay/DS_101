# Multiple inheritance 
#(Parents,adopted parents, relatives)'s attr & methods -> child class
class Parents:
    def parent(self):
        print("This is from parent")

class Adopted_parents:
    def adotped_parents(self):
        print("This is from adopted parents")
    
class Relative:
    def relative(self):
        print("This is from relative")

class Child(Parents,Adopted_parents,Relative):
    def child(self):
        print("This is from child!")

o = Child()
o.adotped_parents()
o.parent()
o.relative()