import random

print("D20 roll program! Let's roll'it up!")

# initial variables
min = 1
max = 20
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling the dice...")
    print("The values are...")
    print(random.randint(min, max))
    print(random.randint(min ,max))

    roll_again = input("Roll the dice again?\n")
    if roll_again:
        print('You chose to not roll the dice again!')