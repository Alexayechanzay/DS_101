class Myclass: #pep8
    def myfun():
        pass

obj1 = Myclass()# constructor
obj2 = Myclass()
# print(obj1,'\n',obj2) #obj1 != obj2

if id(obj1) == id(obj2):
    print("They are same!")
else:
    print("They are different!")