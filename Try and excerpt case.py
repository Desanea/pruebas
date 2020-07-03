#You are running a piece of code but you don't know if it will run right. So you put the code in
#a Try and Excerpt case. If the code dosent' work it goes to the excert case.


try:
    if name>3:
#We haven't defined `name` therefore it will give an error.
        print("Hello")

except:
    print ("There's something wrong with your code - please check again")

#Because the code is faulty, it will go straight to the except case.
#In a nutshell, if the code is fine, no problem, it will run. If not, it will present the excerpt case.

#COMMENTS
#three quoutations marks make comments on long lines
"""
this is a comment
it's multiple lines
this is great
"""
