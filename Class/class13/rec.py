
def info(y):
    i,k,j = y
    z=f"hello i am" + {name} + "my age is " +{age} +"and i am from" + {add}
    print(z)




name = input("enter your name")
age = int("enter the age==")
add = input("give address")
y =(name,age,add)
info(y)