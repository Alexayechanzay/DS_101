class Myclass:
    def __init__(self,xAxis,yAxis):
        self.xAxis=xAxis
        self.yAxis=yAxis

o1 = Myclass(3,5) # o1 -> self 
print(o1.xAxis, o1.yAxis)

o2 = Myclass(1.1,2.2)
print(o2.xAxis, o2.yAxis)