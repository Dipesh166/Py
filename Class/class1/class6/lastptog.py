#tuple inside
output =tuple(())
r=int(input("enter the r="))
c=int(input("enter the c="))
for i in range(r):
    row=()
    for j in range(c):
        column=int(input("enter the value"))
        row=row+(column,)
    output=output+(row,)

print(output)
