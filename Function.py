#A function recalls a code every time you need it. No need to type it again
#Its define by `DEF`

def helloworld():
    print("Hello world")

# DEF=function / helloworld = name of the function / () after each
# function it should end in two brackets. It defines it as
#an empty function or allows the user to inserts some paremeters later in the function.
# PRINT is the code that is going to run

#If we run it now at it is, nothing will happen, but the function will already be recorded in order to use it again.

#In order to call the function we need to type the name of it (helloworld) and the brackets.
helloworld()

#Let's create another function called greeting
def gretting(name):
    print("hi "+ name + "!")

#Now we need to specify the name

gretting("Ramon")

#Now we create a function with the add of two numbers
def resultado(numeros):
    print(2+2)
resultado(5)

def add(num1,num2):
    print(num1+num2)
add(10,15)

def suma(numeros):
    print(5+5)
suma("numeros")

def greeting(pedro):
    print("Hi "+"pedro"+"!")
greeting("pedro")

#RETURN STATEMENT. What the retun statement does in a function is stored it somewhere.
#After that we can associate that statement to a variable

def returnAdd(num1, nume2):
    return (num1 + nume2)
#Variable is going to be `SUM`
#Once python finds the return function it goes back and don't print anything else

sum = returnAdd(12,34)
print(sum)









