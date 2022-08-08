# nested if else


a=int(input("enter the instruction"))

if a==1:
    maths=int(input('Enter the maths=='))
    sciences=int(input('Enter the sciences=='))
    social=int(input('Enter the social=='))
    total = maths+sciences+social
    print("Total marks==",total)
elif a==2:
    maths=int(input('Enter the maths=='))
    sciences=int(input('Enter the sciences=='))
    social=int(input('Enter the social=='))
    total = (maths+sciences+social)*100
    full = 300
    toball = total/full
    print("Percentage %%%=", toball)
    if toball<30:
        print("You are Fail")
    elif toball>=45:
        print("you are pass")