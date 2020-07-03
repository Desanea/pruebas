#There are classes and objects. Classes are the overall type, could be anything, like people
#Farms, teams, etc.
#From that class we got objects, that are related inside the class. It became an
#Instance for that class.
#I.E class= Cars .   Objects= Chevrolet, Chrislers, etc.

#`Self` tells the class which object is perfoming the function.
#`DEF` Defines a function in order to be called later

#Now we create the `person` class defining a couple of methods.
#Class always are upper case!

#INI passes parameters you want to use when you're creating the objects

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getname(self):
        print("Your name is " + self.name)
    def getage(self):
        print("Your age is " + self.age)

p1=Person("bob","22")
p1.getage()
p1.getname()
print("Ta taaaa")

class Monster1:
    def __init__ (self,name,age,power,race):
        self.name=name
        self.age=age
        self.power=power
        self.race=race
    def getname(self):
        print("Your name noble creature is " + self.name)
    def getage(self):
        print("Your age according to our journal is " + self.age)
    def getpower(self):
        print("Your mighty power is " + self.power)
    def getrace(self):
        print("Therefore you are " + self.race)

p1=Monster1("Venonfang", "900 years old", "a breathtaking breath weapon", "Mighty Dragon")
p1.getname()
p1.getage()
p1.getpower()
p1.getrace()

class Monster2:
    def __init__ (self,name,age,power,race):
        self.name=name
        self.age=age
        self.power=power
        self.race=race
    def getname(self):
        print("Your funny name is " + self.name)
    def getage(self):
        print("Your age according to your confession is " + self.age)
    def getpower(self):
        print("Your punny power is " + self.power)
    def getrace(self):
        print("Therefore you're a pitiful " + self.race)

p2=Monster2("Brinky", "20 years old", "a silly pack tactics", "Goblin")
p2.getname()
p2.getage()
p2.getpower()
p2.getrace()
print("My lord...Script finishing executing")












