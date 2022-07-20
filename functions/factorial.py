# factorial finding in python
n=int(input("Enter to find the product of the number"))
product =1
for i in range(n):
    product=product *(i+1)
print(f"factorial of the number =={product}")