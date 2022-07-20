#tuple inside list


a=()
n=int(input("Enter the tuple=="))
r=int(input("Enter the list=="))

for i in range(n):
    b=[]
    for j in range(r):
        c=int(input("enter the list"))
        b=b+[c,]
        a=a+(b,)
        


    
print(a)