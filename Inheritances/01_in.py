# Inheritance examples in python

class Employee: #BASE CLASS
    company="Youtube"

    def showdetail(self):
        print(f"I am employer of the {self.company}")


class Programmer(Employee): #derives class
    language="PYTHON"
    
    def Seedetail(self):
        print(f"I love programming {self.language}")


e=Employee()
p=Programmer()
e.showdetail()
p.showdetail()
p.Seedetail()