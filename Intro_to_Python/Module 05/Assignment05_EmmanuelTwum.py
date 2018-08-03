#-------------------------------------------------#
# Title: Reading and Writing Dictionary Items To/From a Text File
# Dev:   Emmanuel Twum
# Date:  October 29, 2017
#-------------------------------------------------#


#****Data*****

#open the text file in read mode
file = open("C:\_PythonClass\ToDo.txt","r+")

#read the first two lines

strData = file.readline()
strData1 = file.readline()

#convert the existing two lines in the text file to two dictionary rows in a table
dicRow1 = {"Task":strData.split(",")[0],"Priority":strData.split(",")[1]}
dicRow2 = {"Task":strData1.split(",")[0],"Priority":strData1.split(",")[1]}
tblData = [dicRow1,dicRow2]


#***Processing****

#show current table data
def ShowCurrentData():
    print(tblData)
    
#add task to the table
def AddItem():
    while(True):
        #get user input for task and priority
        strTask = input("Please enter a task: ")
        strPriority = input("Please enter the task's priority (low, medium, high): ")
        #convert users inputs into a dictionary row
        dicNewRow = {"Task":strTask.capitalize(), "Priority":strPriority.lower()+"\n"}
        #append current table with new row
        tblData.append(dicNewRow)
        userinput = input("Would you like to continue inputting items? (Y/N) ")
        if(userinput.lower() == 'y'):
            continue
        else:
            break

#Remove item from the table     
def RemoveItem():
    #get user input for removing a task
    strRemoveTask = input("Input the task you would like to remove: ")
    #look up user input in each row in the task column; delete row if found
    for x in tblData:
        if(strRemoveTask.capitalize() == x ["Task"]):
            tblData.remove(x)
            print("Task Deleted")

#save latest data to the text file                  
def SaveData():
    #overwrite current data in the file with new data
    file = open("C:\_PythonClass\ToDo.txt","w")
    #pull values from the dictionary and turn them into a list; save to file
    for x in tblData:
        x.values()
        this_list = list(x.values())
        file.write(this_list[0] + "," + this_list[1])
    file.close()
    

    
#****Input/Output****
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? Input [1 to 5] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice == '1'):
        ShowCurrentData()
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice == '2'):
        AddItem()
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        RemoveItem()
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        SaveData()
        continue
    elif (strChoice == '5'):
        break #and Exit the program    
