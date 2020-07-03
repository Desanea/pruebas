#For Loops are use to pinpoints elements on a list or Tup and do stuff with it

list1 = ("Apples","Cherries","Bananas")
print(list1)
#Then we create a Tuple

tup1 = (13,12,15)
#Now I want to print all the valuables on my list, to do so, I'll use a For Loop. I'm going to call my elements on my list "Item"

for item in list1:
    print(item)

#Now they are printed as items one in each line. I'm assigning valuable "Apple" to my variable "Item". I'll check every
#valuable in the code and print it.
#Now we print the tup:

for item in tup1:
    print(item)

#For loops go thru all the elements on a list or tuple and do something with it, you can do the same with numbers

#Range function. It gives you a series of numbers, going from one index to another index. `i` could be any letter I want.

for i in range(0,10):
    print(i)

#It goes only until the one before the last one! 1-9. If I want to print from 0 to 10

for i in range(0,11):
    print(i)


#Range function have a skip feature! Let's see I want to print all the even numbers in the first 10 numbers
#We put an incoming factor variable at the end, `2`. It goes from 2 from 4

for i in range(0,11,2):
    print(i)

#Now let's try to print the first ten multiple of 5

for i in range(5,26,5):
    print(i)

#Nested For Loops can be used to perform different functions.

for x in range(0,5):
    for j in range(0,3):
        print(x*j)


