# instance attribute 
# Instance object is check first and executed if not than it check to the class and it print the values

class Employee:
    salary=4000

dip=Employee()
kanxu=Employee()

#instance attribute is created 
dip.salary=10000
print(dip.salary)
print(kanxu.salary)