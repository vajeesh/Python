#!/usr/bin/env python
# coding: utf-8

# In[36]:


class Pet:        # Class name Pet given to hold the pet data.
    
    
    def __int__(self, name = '', animal_type = '', age = 0): # constructor method is defined to assign values for name, animal_type, age
        self.__name = name;
        self.__animal_type = animal_type;
        self.__age = age;
        
    def set_name(self, name):                     # Mutator method defined to add name.
        self.__name = name
        
    def set_animal_type(self, animal_type):       # Mutator method defined to add animal_type.
        self.__animal_type = animal_type
        
    def set_age(self, age):                       # Mutator method defined to add age.
        self.__age = age
          
    def get_name(self):                          # Accessor method defined to get name.
        return self.__name
    
    def get_animal_type(self):                   # Accessor method defined to get animal_type.
        return self.__animal_type
    
    def get_age(self):                          # Accessor method defined to get age.
        return self.__age
    
     # A  __str__() method is defined to display the object details in string
    
    def __str__(self):        
        return ('Pet Name :' + self.__name + '\n' + 'Animal Type :' + self.__animal_type +'\n' + 'Age :' + str(self.__age))
    

#created the empty list
pets_list = []                                      
def make_list():               # make_list method created to enter the object attributes 
    try:
        
        t = int(input('No of pets you want to input : '))      
        for i in range(t):     # Created the for loop to enter the no of objects as per the user requirement
            
            x= Pet()
            print("\nEnter details for {} Pet Animals".format(i+1))
        
            # User input values
            x.set_name(input(' Input Pet Name: '))
            x.set_animal_type(input(' Input Animal Type: '))
            x.set_age(int(input(' Input Pet age: ')))
            pets_list.append(x)  # adding all entered values to the list
        return pets_list
    except:
        
        print("Enter the correct integer value")

        
        
def Select_Animal_Type (pets_list):                    #
    print()
    pet_type = input("What type of animal you looking for? :")
    list_1 =[]
    for i in pets_list:
        if Pet.get_animal_type(i) == pet_type:
            list_1.append(i)          
    return list_1
       
    

def display_list(pets_list):                         #display_list  method used to display the elements in the list 
    for item in pets_list:
        print('Pet Name: ',item.get_name())
        print('Animal Type: ',item.get_animal_type())
        print('Pet age: ',item.get_age())
        print()

        
def main():                                           #Main method
    pets = make_list()
    
    try:
        
        while True:                                   # loop creation for the menu2
        
         #menu option is created to display the entire list or the the selected animal type
            print()                              
            print("************** MENU *************")               
            print("1. DISPLAY ENTIRE LIST   :       ")
            print("2. DISPLAY SELECTED ANIMAL TYPE :")
    
            select = int(input("\nENTER THE MENU OPTION    :"))
            if select == 1 :
                print('\nHere is the data you entered:')
                print()
                display_list(pets)
        
            elif select == 2 :
                list_2 = Select_Animal_Type (pets)
                if len(list_2)!=0:
                    for i in list_2:
                        print(Pet.__str__(i))
                        print()

                else:
                    print("the animal type not in the list")    
                
                break
    except:
        print("Enter the correct menu option or check with the input values")
        
if __name__ == "__main__":
    
    main();                #calling the main function

