"""
Recursion Review
author: James Chan
"""

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


if __name__=="__main__":
    #dont use n > 30 for fibonacci, execution time will explode
    n = 4
    print("The {}th element of fibonacci sequence is {}".format(n, fibonacci(n)))
    
    n = 12
    print("The {}th element of fibonacci sequence is {}".format(n, fibonacci(n)))
    
    n = 2
    print("The facotrial of {} is {}".format(n, factorial(n)))
    
    n = 5
    print("The facotrial of {} is {}".format(n, factorial(n)))
    
