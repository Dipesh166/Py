class Number:
    def __init__(self,num):
        self.num=num
        
    def __add__(self,num2):
        print("Operator Overloading...")
        return self.num +num2.num

n1=Number(5)
n2=Number(5)
sum=n1+n2
print(sum)