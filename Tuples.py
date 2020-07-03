tup = ("Oranges","Apples","Bananas")
print(tup)
#We can't modify the values on the list. It's a tuple! but we can access the info on it
print(tup[0])
print(tup[1])

#Index of items on tuple still works as well
print(tup[0:3])
print(tup[0:2])

#You can add tuples together
tup2 = (12,14)
print(tup+tup2)

#You can delete the whole tuple
tup3 =(25,18)
print(tup3)
del tup3


#String function
tup4 = ("Hola")
print(tup4)
print(tup4 * 12)