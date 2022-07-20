# Super method
class Doctor:
    name="bblack"
    def injection(self):
        print("Give me injection")

class Nurse(Doctor):
    
    def injection(self):
        super().injection()
        print("Ok i will give")


class Patient(Nurse):
    
    def injection(self):
        super().injection()
        print("i will take injection")

d=Doctor()
n=Nurse()
p=Patient()
print(p.name)
p.injection()
print(n.name)
