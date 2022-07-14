from datetime import date
from datetime import datetime                          #datetime imported from the datetime module
import datetime
class Note:                                            # Note class is created

    def __init__(self, id, title, text, date, completed, datecomp):    # class attributes are created
        self.id = id
        self.title = title
        self.text = text
        self.date = date
        self.completed = completed
        self.datecomp = datecomp
        
    #mutator method is created to add the attributes    

    def set_id(self, id):
        self.id = id

    def set_title(self, title):
        self.title = title

    def set_text(self, text):
        self.text = text

    def set_date(self, date):
        self.date = date

    def set_completed(self, completed):
        self.completed = completed

    def set_datecomp(self, datecomp):
        self.datecomp = datecomp   

 #accessor method is created to get the attributes   

    def get_id(self):
        return self.id 

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text 

    def get_date(self):
        return self.date 

    def get_completed(self):
        return self.completed

    def get_datecomp(self):
        return self.datecomp
    
 
# note Method created to print the attributes 
    def note(self):
        print ("THE NOTE ID IS: ", self.id)
        print ("THE DATE CREATED IS: ", self.date)
        print (" THE TITLE: ", self.title)
        print (" THE TEXT:", self.text)
        print("Creation Date :", self.date)
        if self.completed:
            print("completed")
            print("Date of Completion", self.datecomp)
        else:
            print("The Note is incomplete.")
    
    



        
    

