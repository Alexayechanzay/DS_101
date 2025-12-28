class Price:
    def payment(self,dataType,*args):#arbitary argument
        if dataType == "int":
            data=0
            count=0
            for i in args:
                count+= 1
                data+= i
            print(f"There are {count} parameter passed")
            return data
        elif dataType == "str":
            data=''
            count=0
            for i in args:
                count+= 1
                data+= i
            print(f"There are {count} parameter passed")
            return data


obj = Price()
print(obj.payment("int",1,2,3,4,5))
print(obj.payment("int",1,10))
print(obj.payment("str","A","B"))
print(obj.payment("str","Alex ","Spencer"))
