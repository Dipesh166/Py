# Constructor in python

class Dev:

    def __init__(self,name,lang,comp):
        self.name=name
        self.lang=lang
        self.comp=comp 

    def detail(self):
        print(f"{self.name}")   
        print(f"{self.lang}")   
        print(f"{self.comp}")    

    def call(self):
        print("So called Developer")


dup=Dev("den","C","google")
dup.detail()