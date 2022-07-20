# factorial from the function and factorail recursive function

from itertools import product


def factorail_fun(n):
    product=1
    for i in range(n):
        product=product * (i+1)
    return product

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)


m=int(input("enter the factorial value =="))
print("factorial" + str(factorail_fun(m)))
print("factorial" + " " +str(factorial_recursive(m)))