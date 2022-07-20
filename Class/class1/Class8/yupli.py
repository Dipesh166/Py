a=()
n=int(input("enter the number=="))
print("Enter the name of students")
for i in range(n):
     b=input("")
     a=a+(b,)

t=tuple(a)
print(t)