from Note import Note                                          # Importing Note class from Note.py file
from datetime import date
from datetime import datetime
import datetime
import pickle

# creating the global constants for menu choice
CREATE_THE_NOTE = 1
READ_THE_NOTE = 2
UPDATE_THE_NOTE = 3
DELETE_THE_NOTE = 4
NO_OF_NOTES = 5
NOTES_COMPLETED_STATUS = 6
SCREEN_ALL_NOTES = 7
Count_date = 8
CHANGE_COMPDATE = 9
SAVEANDEXIT = 10





class Interface:

    
    Note_list= []
    
    def menu():
        try:                    # incase any wrong input value is given try 
                                #and except block ask user to write correct value
            
        
        
            Interface.read()                                             # loop creation for the menu
            while True:
                
                print("*********** MENU *********")               
                print("1. CREATE THE NOTE       :")
                print("2. READ THE NOTE         :")
                print("3. UPDATE THE NOTE       :")
                print("4. DELETE THE NOTE       :")
                print("5. NO OF NOTES           :")
                print("6. NOTES COMPLETED STATUS:")
                print("7. SCREEN ALL NOTES      :")
                print("8. COUNT DATE            :")
                print("9. CHANGE COMPLETED DATE :")
                print("10. SAVE & EXIT          :")
            
                select = int(input("ENTER THE MENU OPTION    :"))
                while select < CREATE_THE_NOTE or select > SAVEANDEXIT:
                    select = int(input('enter a valid choice: '))            # creating the menu selection
                if select == 1 :
                    Interface.CREATE_THE_NOTE()
                elif select == 2 :
                    Interface.READ_THE_NOTE()
                elif select == 3 :
                    Interface.UPDATE_THE_NOTE()
                elif select == 4 :
                    Interface.DELETE_THE_NOTE()
                elif select == 5 :
                    Interface.NO_OF_NOTES()
                elif select == 6 :
                    Interface.NOTES_COMPLETED_STATUS()
                elif select == 7 :
                    Interface.SCREEN_ALL_NOTES()
                elif select == 8 :
                    Interface.Count_date()
                elif select == 9 :
                    Interface.CHANGE_COMPDATE()    
                elif select == 10 :
                    Interface.SAVEANDEXIT()
                           
                    break
        except:

            print("Enter the correct id and run the program")
            

    def read():
        try:
            input_file =  open('notes.txt', 'rb') 
            Interface.Note_list = pickle.load(input_file)                           # by using pickle method list of objects are restored
            input_file.close()                                
        except:
            print("Data couldn't import")                                          # used try and except, if it occurs any error it will run print statement



#Function to save the note (it will save in text doc as binary)            

    def SAVEANDEXIT():
        try:
            output_file = open('notes.txt', 'wb') 
            pickle.dump(Interface.Note_list, output_file)                          # Storing the objects list in the text file
            output_file.close()                                                    # once object is saved in text file it is closed
        except:
            print("Data couldn't save")


#Function to create the note


    def CREATE_THE_NOTE():
        notebook = Note(-1, "title", "text", date.today(), False, date.today())     #  creating the object instance
        if len(Interface.Note_list) == 0:                                           # Automatic id creation for all notes 
            id = 1;
            notebook.set_id(id)                                    
        else:
            lastindex = len(Interface.Note_list) -1
            id = Interface.Note_list[lastindex].id + 1
        notebook.set_id(id)                                        
        notebook = Interface.INPUT_VALUES(notebook)                      
        Interface.Note_list.append(notebook)                                      # Storing the user input values in the list
        notebook.note()                                                           # displaying the user input values
        Interface.SAVEANDEXIT()                                                   # saving once it is created




# Seperate function for the user input values


    def INPUT_VALUES(notebook):
        notebook.set_title(input("Title: "))                                        # User input title
        notebook.set_text( input("Text: "))                                         # User input text
        status  = input("Enter the choice if note is completed or not (Y/N)? ")
        notebook.set_completed(True if status == 'Y' or status == 'y' else False)   # if it is Y or y it will take as true or any other letters it will take as false
        if notebook.set_completed:
                print('the date completed is ', date.today())                       # if notebook is completed it will prints the day when it is completed (it is asked in
                                                                                    # VG part to create the seperate menu for changing the completion date so seperate menu is created)
                                                                                    
                
                notebook.set_datecomp(date.today()) 
        return notebook

                              

#Function to read the note                                   


    def READ_THE_NOTE():

        try:
            
        # this code will be used
            Userid=int(input("Please Enter the ID: "))
            for notebook in Interface.Note_list:                         
                if notebook.get_id() == Userid:                                     # if user id in list
                    notebook.note()                                                 # Prints the user requested id contents from the notebook
                    return notebook                                   

        
            print("The Note was not found in the data.")                            #This will run if no note found with the user entered id  
            return None
        except:
            print("Enter the correct id")
                        
    
                            
        
#Function to update the note           
    
    
    def UPDATE_THE_NOTE():
        try:
            
            Userid=int(input("Please insert the Note ID: "))
            for notebook in Interface.Note_list:                                  # it searches the notebook in the list
                if notebook.get_id() == Userid:
                    notebook = Interface.INPUT_VALUES(notebook)                   # updates the values if id is matched 
                    notebook.note()                                               # returns the updated values
                    return notebook 
            print("The Note was not found in the system.")                        # if id is not found it will run
            return None
        except:
            print("Enter the correct id")
            


# Function to delete the note created


    def DELETE_THE_NOTE():
        try:
            
            Userid=int(input("Please insert the Note ID: "))
            for notebook in Interface.Note_list:                                      # it searches the notebook in the list
                if notebook.get_id() == Userid:
                    notebook = Interface.Note_list.remove(notebook)                   # removes the notebook from the list
                    print('The Respective note is deleted')                           # prints the statement once it is deleted 
                    return notebook                         
            print("The notes was not found in the system.")                            # if id is not found it will run
            return None
        except:
            print("Enter the correct id")


            
# Function to find the no of days took for completion
    def Count_date():
        try:
            
            Userid=int(input("Please insert the Note ID: "))
            for notebook in Interface.Note_list:                                      # it searches the notebook in the list
                if notebook.id == Userid:
                    if(notebook.get_completed()):
                        date = (notebook.datecomp - notebook.date).days                   #counts the completed date
                        print(date)                                                       # prints the completed date
                        return notebook
                    else:
                        print ("the note is not completed")                                     # if it is not completed it prints the statement  
                
        
        except:
            
            print("Enter the correct id")
            

# It is asked to create the seperate menu for changing completion date in VG part so it is created

    def CHANGE_COMPDATE():
        Userid=int(input("Please insert the Note ID: "))
        for notebook in Interface.Note_list:                                         # it searches the notebook in the list
            if notebook.get_id() == Userid:
                if notebook.set_completed:
                    date = input("Enter date in YYYY-MM-DD format: ")
                    year, month, day = map(int, date.split('-'))                 
                    date = datetime.date(year, month, day)                           # if notebook is completed it will prints the day when it is completed
                                 
                    n= notebook.set_datecomp(date)
                                                          
                    Interface.Note_list.append(n)
                    notebook.note()
                    Interface.SAVEANDEXIT()
                    
                return notebook




            

#Function to check the no of notes created VG part

    def NO_OF_NOTES():
         if len(Interface.Note_list) == 0:                                            # checks the length of Note_listequals 0
            print('No Notes in Database')                                             # prints the statement   
         else:
            print("Total No Of Notes in a Database : ",len(Interface.Note_list))      # it counts the no of notes in database and prints the total note in a database
            print('\n')


#Function to display all notes VG part


    def SCREEN_ALL_NOTES():
        if len(Interface.Note_list) == 0:                                            # checks the length of Note_listequals 0
            print('No Notes in Database')
        else:
            for i in Interface.Note_list:
                i.note()

 # Function to check the note completed status VG part   
    def NOTES_COMPLETED_STATUS():
        if len(Interface.Note_list) == 0:
            print('No Notes in Database')                                                        # prints the statement if length of list is 0
        else:
            uncomplete_notes = sum(not notebook.completed for notebook in Interface.Note_list)   # counts number of no.of notes yet to be completed
            
            Total_notes = len(Interface.Note_list)                                               # counts the no of notes created in the list using len()
                                                      
            Pending_notes_percentage = str(round((uncomplete_notes/Total_notes)*100)) + "%" if Total_notes else "NA" # Percentage of notebook which is not completed

            
            print(" Total No Of Notes:",Total_notes,
                  "\n","TOTAL NO OF UNCOMPLETED NOTES: ",uncomplete_notes, "\n","PENDING NOTES PERCENTAGE:",Pending_notes_percentage)    





   

    
