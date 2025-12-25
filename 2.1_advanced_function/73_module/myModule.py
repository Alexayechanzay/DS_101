def fibo(n):
    """Normal fibonacci sequence"""
    a,b = 0,1
    while a < n:
        print(a,end=' ')
        a,b = b,a+b # fibonaci 
        
#fibo(3)

def listFibo(n):
    """List fibonacci sequence"""
    result=list()
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b =b,a+b
    return result # result stores the fibonacci seq

#print(listFibo(3))
