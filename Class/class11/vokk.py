n=int(input("enter the number=="))
for i in range(2,n):
    if n%i==0:
        print(n,"is compatible")
        break
else:
    print(n,"is prime no")



