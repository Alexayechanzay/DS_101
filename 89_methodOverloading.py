class Price:
    def payment(self, *args):#arbitary argument
        data=0
        count=0
        for i in args:
            count+= 1
            data+= i
        print(f"There are {count} parameter passed")
        return data

obj = Price()
print(obj.payment(1,2,3,4,5))
print(obj.payment(1,10))
print(obj.payment("A","B"))
