class Monsters:
    def __init__(self):
        pass
    def size1(self):
        print("No worries.This creature is small")
    def size2(self):
        print("Careful.This creature is large")
    def size3(self):
        print("Watch out! This creature is huge")

m=Monsters()
m.size1()
m.size2()
m.size3()

class Kobold(Monsters):
    def __init__(self, name, affiliation):
        self.name=name
        self.affiliation=affiliation
    def getname(self):
        print("Your name is " + self.name)
    def getaffiliation(self):
        print("You belong to the " + self.affiliation)

k=Kobold("Kiplik", "Clan of the stormy cave")
k.getname()
k.getaffiliation()
k.size1()


