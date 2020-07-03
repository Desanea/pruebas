#There's a parent class and a child class. The child claas inherance all the properties
#of the parent class.
#i.e Parent class = monsters
#child class = Kobolds, Dragons, wererats, etc.

class Parent:
    def __init__(self):
        print("This is the parent class")
    def parentfun(self):
        print("This is the parent function")
p=Parent()
p.parentfun()

#Now we create the child class. In brackets we put the name of the
#Parent class. This states that the child inherence the parent features.

class Child(Parent):
    def __init__(self):
        print("This is the child class")
    def childfunc(self):
        print("This is the child func")

#Now we create a child.
c=Child()
c.childfunc()

#Now I can call the parent function on my child class.
#When we create the child object, this child object inherance the features of
#the parent class as well.

c.parentfun()

#Now let's try an overwriting method. If I have a parent class, and child class
#and both of them have the same functions, how do I tell Python I want to use the
#parent class function and not the child
#So let's create a new parent class
class Parent:
    def __init__(self):
        pass
    def test(self):
        print("parent")

p=Parent()
p.test()

#Now let's create a child class
#But also I'm creating a test function for my class.

class Child(Parent):
    def __init__(self):
        pass
    def test(self):
        print("child")

#Now I create a child object.
#All this will re-initialize it. Whatnever code I put over here will
#overwrite the code I had before. 

c=Child()
c.test()




