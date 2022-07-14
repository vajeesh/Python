#!/usr/bin/env python
# coding: utf-8

# In[13]:


# Exercise 1: Personal Information Class


# Class name Personal_Information given to hold the personal data.

class Personal_Information:         #In question title it given Personal Information so same is given to class 

       
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

   
    def set_name(self, name):    # Mutator method defined to add name.
        self.__name = name

   

    def set_addr(self, address): # Mutator method defined to add address.
        self.__addr = address

    

    def set_age(self, age):      # Mutator method defined to add age.
        self.__age = age

    

    def set_phone_number(self, phone_number):   # Mutator method defined to add phone no.
        self.__phone_number = phone_number

   

    def get_name(self):           # Accessor method defined to get name.
        return self.__name

   

    def get_address(self):        # Accessor method defined to get address.
        return self.__address

    
    def get_age(self):           # Accessor method defined to get age.
        return self.__age

   
    def get_phone_number(self):   # Accessor method defined to get phone no.
        return self.__phone_number

    # A  __str__() method is used to display the object details in string
    
    def __str__(self):
        return 'NAME: ' + self.__name + '\n' + 'ADDRESS: ' + self.__address + '\n' + 'AGE: ' + str(self.__age) + '\n' + 'PHONE NUMBER: ' + self.__phone_number




    
myinfo = Personal_Information(" Maha", "Borlange, Sweden", 23, "875419476")      #My Personal information values given to the object myinfo
friendinfo = Personal_Information("Daniel", "Falun, Sweden", 23, "789456123")    #Personal information of my Friend given to the object friendinfo
brotherinfo = Personal_Information("Martin", "Lund, Sweden", 18, "897456123")    #Personal information of my Brother given to the object brotherinfo

print('My Personal information\n')
print(myinfo)
print("\nPersonal information of my Friend\n")
print(friendinfo)
print("\nPersonal information of my Brother\n")
print(brotherinfo)
        
        

