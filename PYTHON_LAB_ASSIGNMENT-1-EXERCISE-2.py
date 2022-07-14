#!/usr/bin/env python
# coding: utf-8

# ## Exercise 2

# In[ ]:


# A county collects property taxes on the assessment value of property, which is
# 60 percent of the property’s actual value.
# For example, if an acre of land is valued at $10,000, its assessment value is
# $6,000.
# The property tax is then 72¢ for each $100 of the assessment value. The tax
# for the acre assessed at $6,000 will be $43.20.
# Write a program that asks for the actual value of a piece of property and displays the assessment value and property tax.


# In[1]:


property_value = float(input("ENTER THE PROPERTY VALUE : "))   # This program will calculate the assessment value and property tax of user input property value
av = 0.60 * property_value     #Formulat to calculate the assessment value which is 60% of property value
property_tax = (av*0.72) / 100   # formula to calculate the property tax which is 75 cents for 100$
print("THE ASSESSMENT VALUE IS : ", av,'$')
print("THE PROPERTY TAX IS : ", property_tax, '$')

