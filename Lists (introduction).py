#LISTS
#A comma separate valuables that allows us to access any item based on the index
#List uses the [] symbols.
#Tuples uses ()

#Let's make a shopping list
shoplist=["Apples", "Oranges", "Bananas", "Cheese"]

print(shoplist)

#Now, how we access a valuable? The index starts by number 0, meaning item number 1 is
#actually number 0. Now let's print the first item on the list

print(shoplist[0])

#Now let's print the third item

print(shoplist[3])
#Also we can shortlist the list itself
#Number ends one number short of the one desired

print(shoplist[0:3])

#Let's now update the list, changing some items. Let's add an item
#In order to do so we use the APPEND function

shoplist.append("Blueberries")

#Now that item is added, let's print it again
print(shoplist)

#Now let's remove apples from the list and add cherries
#So we state that the first item on muy list (apples) are now are cherries
shoplist[0] ="Cherries"
print(shoplist)

#Now I want to delete one item, the oranges
#We use the DELETE method
del shoplist[1]
print(shoplist)

#How many items are in my shop list?
#We use the LEN function

print(len(shoplist))

#Let's create another list
shoplist2 = ["Bread", "Jam", "Peanut butter"]
print(shoplist2)

#Now let's combine this two list together
print(shoplist)
print(shoplist2)
print(shoplist + shoplist2)

#Now let's multiply the list
print(shoplist*2)

#Now we create a list and on it we want to find the highest number on it
#We use the MAX function
listnum = [1,4,7,2,23,6]
print(max(listnum))

#Now I want to find the smallest value
#I use the MIN function
print(min(listnum))













