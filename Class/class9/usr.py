# user defined dictionary
info ={}
n=int(input("Enter the vslue="))

for i in range(n):
    name=input("Enter the name =")
    phone=int(input("Phone number=="))

    info[name]=phone
print(info)