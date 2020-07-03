#PlACEHOLDERS
#Take the place of something to be replace.
# %s stands for a string
# %d stands for a digit

name="Jake"
print(name + " is 15 years old")

#Now, there's an easy way to do this, an it's using placeholders:
#the %s symbols is the placeholder where we want to put the data

sent = "%s Is 15 years old"

#Now we want to put the name Jake into it

print(sent%name)

#We can put anything we want. The symbol indicates the value we want to sustitue.
print(sent%"ramon")

#Now, what happens if there's two variables?

sent="%s %s is the president of the US"
#Now we can set both valuables

print(sent%("Barack","Obama"))

#Now let's specify the person and the age. We use the placeholder for string and
#digit

sent= "%s is %d years old"
print(sent%("Obama", 50))









