#!/usr/bin/env python
# coding: utf-8

# ## Exercise 1

# In[ ]:


# Write a program that asks the user to enter a distance in miles, then converts
# that distance to Kilometer and present the kilometers.
# The conversion formula is as follows: Miles=Kilometers×0.6214


# In[2]:


def  Miles_Converter():   # by using the miles converter function it will display the distance in kilometer for the usuer input distance in miles
    
    miles = float(input("ENTER THE VALUE FOR THE DISTANCE IN MILES : "))
    km = miles / 0.6214
    print ("THE DISTANCE IN KILOMETER IS: ", km)
    return km
    
    
Miles_Converter()    

