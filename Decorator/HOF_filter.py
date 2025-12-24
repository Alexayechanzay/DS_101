def starts_a(w):
    return w.startswith("a")

li = ["apple", "banana", "avocado", "cherry", "apricot"]
res = filter(starts_a, li)
print(list(res))

#retruning only even numbers
num = [1,2,3,4,5,6,7,8,9,10]
even_num = list(filter(lambda x: x%2==0,num))
print(even_num)


# filter and transform 
a = [1, 2, 3, 4, 5, 6,7,8,9,10]
b = list(filter(lambda x:x%2==0,a))
evenSquare = list(map(lambda x:x**2,b))
print(evenSquare)