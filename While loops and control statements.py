#Loops that continues until the condition turns false

c = 0
while c<5:
    print(c)
    #If we allow this line to end here, Python will print endlessy, because 5 will always be more that C.
    #In order to stop the statement to be true we put the following line:
    c=c +1
#c=c + 1 means that that the list goes one by one, if you put `2` it will go, two by two, 1,2,4

print(c)

#The're three control statements in While Loops: Break, Continue, Pass
#They change the path that loops normally takes

#BREAK
#uses the command `IF` if the number equals this, stop it!
c=0
while c<5:
    print(c)
    if c== 3:
        break
        #How I want to run it? As this:
    c=c +1
print(c)

#CONTINUE
#if you want to skip a number or data, use continue and the code will skip that part and
#keep running. In other words, ignore number 3 and keep running the code. Skip the remaining code and go back
#to the start of the loop

c = 0
while c < 5:
    c = c + 1
    if c == 3:
        continue
    print(c)

#PASS
#It's a filler code. If you don't know yet what are you going to write on that line of code, you can save the space
#until you know






