# multidimesional 
output=[]
n=int(input("enter the number "))
for i in range(n):
    name=input("enter the name")
    addressno=int(input("enter the address"))
    place=input("enter the place")
    info=[name,addressno,place]
    output.append(info)

print(output)  
          
