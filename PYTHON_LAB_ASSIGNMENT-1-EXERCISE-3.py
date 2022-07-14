#!/usr/bin/env python
# coding: utf-8

# ## Exercise 3

# In[ ]:


# Write a function named my_max that accepts two integer values as arguments
# and returns the value that is the greater of the two. For example, if 12 and 19
# are passed as arguments to the function, the function should return 19. Use
# the function in a program that prompts the user to enter two integer values.
# The program should display the value that is the greater of the two


# In[4]:


def my_max(x,y):     #using my_max function and if loop it will calculate the greater number of two user input numbers
    if x > y:
        print ('THE GREATER VALUE OF THE TWO ENTERED VALUE IS ',x)
    elif x < y:
        print ('THE GREATER VALUE OF THE TWO ENTERED VALUE IS ',y)
    elif (x==y):
        print('THE GREATER VALUE OF THE TWO ENTERED VALUE IS ', x)  # if both no is same it will enter x value
        
x = int(input("please enter the value of x: "))   
y = int(input("please enter the value of y: ")) 

my_max(x,y)

