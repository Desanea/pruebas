#In case something happens,then this happens. ie. if it's raining, I take an umbrella, if not, then I stay home
#If it's true, the code will run, if the statement is false, then another code will run.
if (5>3):
    print("Hello")

#Now's let's use a case where the condition is not true
if (3<2):
    print("Hello")
else:
    print("The condition is not true")

#The conditions and functions should be typed in the format showed above!

#Also you can compare variables, numbers, etc, in order to see if they are true or false. Always use
#double signs!! One single = means `equal` two== make compare!
print(3>=2)
print(3<=2)
print(3==3)

#To know if something IS NOT equal to other thing we do the following:
print(3 !=2)

#List of relational operators (6 en total)
# > < (greater / less then)
# >= <= greater than equal to / less than equal to
# == equal to equal to,
# != not equal to

#ELIF
#Allows you to have multiple statements (always remember : after `else` and at the end of `elif`
#`ELSE` if first conditions are not true, then run ELSE
age=16
if (age<13):
    print("You are young")
elif (age >=13 and age < 18):
    print("You are a teenager")
else:
    print("You are an adult")

#`AND` combines conditional statements. If both conditions are true, the code will run

if (5> 3 and 2>1):
    print("Eureka!")

#`OR` condition. If one is true, only one, then it will run the code

if (5>3 or 2>1):
    print("True")



