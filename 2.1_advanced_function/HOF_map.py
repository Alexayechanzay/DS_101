strings = ['1','2','3','4','5']
digits = list(map(int,strings))
#Explanation: map() applies int() 
# to each element in s which changes 
# their datatype from string to int.
# map() function returns a map object, 
# which is an iterator.
print(digits)

square = list(map(lambda x: x**2,digits))
print(square)

# map func with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))