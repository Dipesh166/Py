# objects and class examples
class School: #class
    formType = "School Form"
    def printData(self): #function
        print(f"Student name is {self.name}")
        print(f"Student name is {self.faculty}")


obj=School() #object declared
obj.name="dipesh"
obj.faculty="sciences"
obj.printData()
