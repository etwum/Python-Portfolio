# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:14:17 2017

@author: Emmanuel
"""

#boolean variable for while loop
boolNoErrors = False

#while loop will continue until the user inputs valid values
while(boolNoErrors != True):
    
    #Begins the exception handling block 
    try:
        #User inputs two values
        fltNum1 = float(input("Please enter your first number: "))
        fltNum2 = float(input("Please enter your second number: "))
        
        #Performs division based on the user inputs
        division = fltNum1/fltNum2
        
    #Checks for ValueError and ZeroDivision Error
    except (ValueError, ZeroDivisionError) as x:
        #prints the statements below
        print("The following error has occurred: ")
        
        #prints the default Python error code
        print(x)
        print("\nPlease try again!")
    
    #if the user inputs are valid the else statement is performed
    else:
        #prints the results of dividing the numbers
        print("Your numbers divided: ", division)
        #ends the loop
        boolNoErrors = True
        
        
    