#Class Methods

class Emp:
    name="dip"
    salary=1000

    @classmethod
    def changeSal(cls,sal):
        cls.salary=sal

e=Emp()
print(e.salary)
e.changeSal(45454545)
print(e.salary)
print(Emp.salary)