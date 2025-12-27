# crud = create read update delete
# 1.manually 2.built-in
# 1.manually -> 1.1.using update method in class, 1.2.holding class const

class Myclass:
    def __init__(self):
        self.name = "Alex"
        self.age = 18
        self.hobby = "Competitive programming"
    
    def update(self):
        self.name = "ACZ"
        self.age = 17;
        self.hobby = "English"

o1 = Myclass()
o2 = Myclass()
print("Before update")
print("object 1's default values: ",o1.name, o1.age, o1.hobby)
print("object 2's default values: ",o2.name, o2.age, o2.hobby)

# manually updating 
o1.name = "Aye Chan Zay"
o1.age = 20
o1.hobby = "Programming"

o2.name = "Alex Spencer"
o2.age = 19
o2.hobby = "Physics"

print()
print("After manual update")
print("object 1's updated values: ",o1.name, o1.age, o1.hobby)
print("object 2's updated values: ",o2.name, o2.age, o2.hobby)