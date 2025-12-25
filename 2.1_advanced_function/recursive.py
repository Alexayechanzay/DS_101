# factorial using recursive 
def factorial_recursive(n):
    # if n<=1 : # base case
    #    return 1
    # else:
    #   return n * factorial_recursive(n-1) # Recursive step
    
    
    return 1 if n<= 1 else n * factorial_recursive(n-1)

print(factorial_recursive(5))