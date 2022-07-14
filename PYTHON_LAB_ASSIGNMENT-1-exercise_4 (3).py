#!/usr/bin/env python
# coding: utf-8

# ## Exercise 4 Test Average and Grade

# In[ ]:


# Write a program that asks the user to enter five test scores. The program should
# display a letter grade for each score and the average test score. Write the
# following functions in the program:
# • calc_average This function should accept five test scores as arguments
# and return the average of the scores.
# • determine_grade This function should accept a test score as an argument and return a letter grade for the score based on the following grading scale:
# Score Letter Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# Below 60 F


# In[11]:


try:                                               # Marks for the five test score is entered by the user input. 
                                                   #try is used to eliminate the non float value

    MARK_1 = float(input("PLEASE ENTER SCORE 1: ")) #sometimes marks may be entered in floats so float is given
    MARK_2 = float(input("PLEASE ENTER SCORE 2: "))
    MARK_3 = float(input("PLEASE ENTER SCORE 3: "))
    MARK_4 = float(input("PLEASE ENTER SCORE 4: "))
    MARK_5 = float(input("PLEASE ENTER SCORE 5: "))
    
    StudentScore = MARK_1, MARK_2, MARK_3, MARK_4, MARK_5
    

    def determine_grade(StudentScore):       # For assigning the grades for the each marks and average marks the function name determine_grade is used 
                                             # And by using if and elif loop grades are assigned.
        if StudentScore>=90 and StudentScore<=100:
            grd = "A"
        elif StudentScore>=80 and StudentScore<=89:
            grd = "B"
        elif StudentScore>=70 and StudentScore<=79:
            grd = "C"
        elif StudentScore>=60 and StudentScore<=69:
            grd = "D"
        elif StudentScore>=0 and StudentScore<60:  #The score between 0 to 59 will print F 
            grd = "F"
        else:
            print("ENTER THE CORRECT SCORE VALUE!")    #if the entered value is negative it will print this value
        return grd

    def calc_average(MARK_1, MARK_2, MARK_3, MARK_4, MARK_5):  # This function will calculate the avereage of five marks 
        avg = (MARK_1+MARK_2+MARK_3+MARK_4+MARK_5)/5     # The purpose of not rounding is if one of 5 score is entered as 59 which will give the average grade as pass 
        print ("\nTHE AVERAGE OF 5 TEST SCORE\t\tAVERAGE GRADE")
        print (str(avg), "\t\t\t\t\t", determine_grade(avg))   # This will write the average and grade for the average test score
    calc_average(MARK_1, MARK_2, MARK_3, MARK_4, MARK_5)       

    def result_table(MARK_1, MARK_2, MARK_3, MARK_4, MARK_5):   # This function will print the scores and grade for the each test score
        print("\nScore\tLetter Grade")
        print(str(MARK_1),'\t',determine_grade(MARK_1),'\n',              str(MARK_2),'\t',determine_grade(MARK_2),'\n',              str(MARK_3),'\t',determine_grade(MARK_3),'\n',              str(MARK_4),'\t',determine_grade(MARK_4),'\n',              str(MARK_5),'\t',determine_grade(MARK_5),'\n',sep='')  # this will print score and letter in row wise
    result_table(MARK_1, MARK_2, MARK_3, MARK_4, MARK_5)

       
except :
    print("Wrong variable,",
          "please supply an integer next time!",
          sep = '\n')                                       # if the value is non integer or float value it will print the above statement

