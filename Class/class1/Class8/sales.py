#daily sales record
sales="today sales"
n=int(input("Enter the n="))
for i in range(n):
    name=input("enter the product name:")
    quantity=input("enter the product quantity:")
    price=int(input("ENTER THE PRICE"))

    info=f"\nProduct NAME ::{name}-----qUANTITY::{quantity}----price::{price}\n"
    student =sales + info
    print(student)

