i={}
i=0
all_total=0
n=int(input("enter the vlaue of n"))
while i<n:
    name=input("Enter name==")
    price=int(input("quality prices=="))
    quantity=input("enter the quantity")
    total=price*quantity

    info="name+" "+str(price)+" "+str(quantity)" " +sr(total)"
    s=s+info
    all_total=all_total + total
    i =i+1
print("the bill is \n",s)
print('ALL total is =',all_total)

.