# Mutliple inheritance in the python
class Employe:
    name="dipesh"
    level=0

    def showleb(self):
        self.level=self.level+1

class Lang:
    language="Python"
    ach="National Award"


class Programmer(Employe,Lang):
    dev="Django developer"


p=Programmer()
print(p.name)
p.showleb()
print(p.level)
print(p.dev)
print(p.language)
print(p.ach)
