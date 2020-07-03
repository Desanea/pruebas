class Cleric:
    def __init__(self):
        pass
    def size1(self):
        print("Name:", "Waldorf")
    def size2(self):
        print("Cleric", "Level 1")
    def size3(self):
        print("Number of attacks 1.","Proficiency bonus +2.","STR score 18.","STR modifier +4")
    def size4(self):
            print("Base attack +6")
    def size5(self):
        print("Weapon of choice: Mace. Damage: 1D6 Bludgeoning")


m=Cleric()
m.size1()
m.size2()
m.size3()
m.size4()
m.size5()

print("Simulate attack roll vs monster with AC 15:")

print("Roll of D20= 6+10=16")


if (16>15):
    print("Waldorf hits!")

print("New attack roll")
print("Roll of D20= 3+1")

if (4<15):
    print("Waldorf miss!")
else:
    print("Now we are talking!")

print("New attack roll")
print("Roll of D20=20")

if (20>15):
    print("Critical hit!")
else:
    print("Normal hit")






