class People:
    def __init__(self,id,age):
        self.id = id
        self.age = age

    def __add__(self,self1):
        id_sum = self.id + self1.id 
        age_sum = self.age + self1.age 
        return id_sum,age_sum

int 
p1 = People(100,1)
p2 = People(101,10)
p3 = People(102,20)

total_idAge = p1+p2
Final_total = total_idAge + p3
print(total_idAge)

