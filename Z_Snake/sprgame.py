#sissor papper rock game 
# sissors (s) papper(p) and rock(r)
import random



def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=="s"  :  
        if you=='p':
            return False
        elif you=='r':
                return True
    elif comp=='p':
        if you=='r':
            return False 
        elif you=='s':
            return True                
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True  






print("Comp turn sissors(s) papper(p) and rock(r)")
randNo = random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='r'    




you=input("Your turn turn sissors(s) papper(p) and rock(r)==")

a=gameWin(comp,you)
print(f"computer choose = {comp}")
print(f"You choose = {you}")
if a==None:
    print('you are tie!!!!!!!!')
elif a:
    print('you win !!!!!!!')
else:
    print("you lose !!!!!!!!!")
