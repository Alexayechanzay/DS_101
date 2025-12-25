def mydec1(fn):
    def inner():
        print("Running decorator 1")
        return fn()
    return inner

def mydec2(fn):
    def inner():
        print("Running decorator 2")
        return fn()
    return inner

# Alt to result = mydec1(mydec2(myfun))
@mydec1
@mydec2
def myfun():
    print("Working function: myfun")

myfun()