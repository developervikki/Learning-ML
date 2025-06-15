def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
    #5=>5*4*3*2*1
    
def print_factorial(n):
        result=factorial(n)
        print(f"The factorial of {n} is {result}")
        
print_factorial(5)