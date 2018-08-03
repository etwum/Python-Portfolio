# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 16:34:50 2017

@author: Emmanuel
"""
#****Add Error Handling code to the lab 7-1 code
dicRow = {}
tblData = []
ID = 1

def LoadData():
    try:
        file = open("Test.txt","r")
        for line in file:
            strData = line
            dicRow = {"ID":strData.split(",")[0],"Product":strData.split(",")[1],"Price":strData.split(",")[2]}
            tblData.append(dicRow)
    except FileNotFoundError as x:
        print("The following error occurred: ")
        print(x)
        
def ShowCurrentData():
    return print(tblData)

def AddData():
    ID = 1
    while(True):
        
        ID += 1
            #get user input for task and priority
        strProduct = input("Please enter the name of the item purchased: ")
        try:
            fltPrice = float(input("Please enter the price: "))
        except ValueError as x:
             print("The following error occurred: ")
             print(str(x) + "\n")
             print("Please try again by inputting a number")
             break
        #convert users inputs into a dictionary row
        dicNewRow = {"Name":ID, "Product":strProduct.capitalize(), "Price":str(fltPrice) + "\n"}  #, #"Name":strProduct, "Price":fltPrice}
            #append current table with new row
        tblData.append(dicNewRow)
        userinput = input("Would you like to continue inputting items? (Y/N) ")
        if(userinput.lower() == 'y'):
            continue
        else:
            try:
                file = open("Test.txt","w")
                for x in tblData:
                    x.values()
                    this_list = list(x.values())
                    print(this_list)
                    file.write(str(this_list[0]) + "," + this_list[1] + "," + this_list[2])
            except FileNotFoundError as x:
                print("The following error occurred: ")
                print(x)
                file.close()
                break
         
        
LoadData()    
    
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? Input [1 to 5] - "))
    print()#adding a new line
    
    
    # Step 3 -Show the current items in the table
    if (strChoice == '1'):
        ShowCurrentData()
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice == '2'):
        AddData()
        continue
    elif (strChoice == '3'):
        break #and Exit the program   