#calculator from the functions
def main():
 a=int(input("enter the value of a ::"))
 b=int(input("enter the value of b::"))
 o=input("enter the parameter for op of o ::")

 def add(a,b):
    print(a+b)

 def sub(a,b):
    print(a-b)

 def mul(a,b):
    print(a*b)

 def div(a,b):
    print(a/b)

 def calc(a,b,o):
    if o=="+":
        add(a,b)
    elif o == "-":
        sub(a,b)
    elif o =="*":
        mul(a,b)
    elif o=="/":
        div(a,b)
    else:
        print("INVLAID ERROR !!!!!!!!!!!!!!")



 calc(a,b,o)
 REPEAT = input("Would you like to run again==").lower()
 if REPEAT == 'yes':
        main()
 else:
    print("bye")
    exit()
main()

