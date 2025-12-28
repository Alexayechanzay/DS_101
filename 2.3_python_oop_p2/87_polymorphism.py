# different classes but same methods
class Alex:
    def human(self):
        print("Alex is a Computer Scientist")
        print("Alex loves programming")

class Spencer:
    def human(self):
        print("Spencer is a Mathematican")
        print("Spencer loves problem-solving")

class ACZ:
    def human(self):
        print("ACZ is a Theoritical Physicist")
        print("ACZ loves critical-thinking")

class People:
    def chose_human(self,obj):
        obj.human()

alex = Alex()
spencer = Spencer()
acz = ACZ()
p = People()
#p.chose_human(alex) #alex is a obj

mylist = [alex,spencer,acz]
for i in mylist:
    p.chose_human(i)
    print()
