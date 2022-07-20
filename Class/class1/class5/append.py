# keeping 
output=[]
total=[]
n=int(input('enter the value of n=='))
for i in range(n):
    name=input("enter the name==")
    price=int(input("enter the price"))
    qulaity=int(input("ente the quality"))
    total=price * qulaity
    info=[name,price,qulaity]
    output.append(info)
    info.append(total)
print(output)

for i in range(n):
    print('Total:', output[i][3])