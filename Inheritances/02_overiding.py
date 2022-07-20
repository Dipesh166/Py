# Overiding in the Python

class Employee:
    company="Googel"
    def show(self):
        print(f"I am here ")


class Winner(Employee):
    def show(self):
        print("I am Base class ")


e=Employee()
w=Winner()
e.show()
w.show()