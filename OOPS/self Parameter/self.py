# self parameter best example

class Student:
    school="Toran"
    
    def bill(self,greetings):
        print(f"ROSHAN FEES IN {self.school} School  ==={self.fee}\n {greetings} ")
    
    @staticmethod
    def greet():
        print("=============!!!!!!!FEES ALERT!!!!!!!================")

roshan=Student()
roshan.fee=50000000000000
roshan.greet()
roshan.bill("PAY FAST")