#dictionary inside list
items=[]
n=int(input("Enter the number::"))
for i in range(n):
    name=input("enter the name::")
    rate=int(input("enter the rate::"))
    quantity=int(input("enter the qunantity::"))
    total=quantity*rate
    i={"name":name,"Rate":rate,"Quatity":quantity}
    items.append(i)
print(items)
