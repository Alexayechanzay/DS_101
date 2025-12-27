# 5 built-in attr in class
#__dict__ (to access all info)
#__doc__ (to access doc strings)
#__name__ (to access class name)
#__module__ (to access the class relavent modules)
#__bases__ (INHERITANCE)
class Myclass:
    """Myclass"""
    var = "programming"
    def active():
        print(f"Hello from {Myclass.var}")

#print(Myclass.__dict__)
for key,value in Myclass.__dict__.items():
    print(f"{key}:{value}")

