import random
print("D20 roll program... Ready to roll for you!")

#Initial variables
crit_miss = 1
crit_hit= 20
roll_again= "yes"
#rolled_d20 = random.randint(crit_miss, crit_hit)

while roll_again == "yes" or roll_again == "y":

    #print("The dice is rolling...")
    #print("And you got...")
    rolled_d20 = random.randint(crit_miss, crit_hit)
    print('You rolled: {}'.format(rolled_d20))

    #if  random.randint == crit_hit:
        #print("Critical Hit! Way to go!")
    if rolled_d20 == crit_hit:
        print("Critical Hit! Way to go!")

    #if  random.randint == crit_miss:
    if rolled_d20 == crit_miss:
        print("Critical miss")

    #if  (random.randint == (crit_miss)):
        #print("Ah, critical miss, that's sucks, try again!")


    else:
        print("Nice, but you really need a critical hit! They're soooo good!")

    roll_again = input("Want to roll again?\n")

while roll_again == "no" or roll_again == "n":

    if roll_again:
        print("Thanks for using our shareware program, but...Are you sure you don't want to temp luck and roll again?")
        print("You can get a critical! come on, play the program again Sam!")
        print("And don't listen to that `process finished with exit code 0`, crap! Nothing is finished until")
        print("you roll a smashing and glorious Critical Hit! Try again!")

    break






