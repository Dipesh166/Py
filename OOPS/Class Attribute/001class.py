# Class attribute and changing of the class attribute

class Employee: #class
    company="GOOGLE"


dipu=Employee() #object
kanxu=Employee()
print(dipu.company)
print(kanxu.company)

Employee.company="YOUTUBE" # changing class attribute

print(dipu.company)
print(kanxu.company)