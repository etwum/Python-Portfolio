#-------------------------------------------------#
# Title: Using Functons to Read/Write Dictionary Items To/From a Text File
# Dev:   Emmanuel Twum
# Date:  November 3, 2017
#-------------------------------------------------#


#****Data*****

#declare a variable file
file = ()
#create blank table
tblData = []


#***Processing****
class ToDoList(object):
#includes methods defined in the class

    @staticmethod
    def LoadData():
        """reads text file then converts the current lines to dictionary rows in a table"""
        #open the text file in read only mode
        file = open("C:\_PythonClass\ToDo.txt","r+")
        
        #convert each row in the text file to a dictionary; append each dictionary into a table
        for line in file:
            strData = line
            dicRow = {"Task":strData.split(",")[0],"Priority":strData.split(",")[1]}
            tblData.append(dicRow)
    
    @staticmethod
    def ShowCurrentData():
        """show current table data"""
        return print(tblData)
        
   
    @staticmethod
    def AddItem():
        """add task to the table"""
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
    
    
    @staticmethod    
    def RemoveItem():
        """Remove item from the table"""
        boolTask = False
        #get user input for removing a task
        strRemoveTask = input("Input the task you would like to remove: ")
        #look up user input in each row in the task column; delete row if found
        for x in tblData:
            if(strRemoveTask.capitalize() == x ["Task"]):
                tblData.remove(x)
                print("Task Deleted")
                boolTask = True
        if(boolTask == False):
            print("Task not Found")
                
    
    @staticmethod              
    def SaveData():
        """save latest data to the text file"""
        #overwrite current data in the file with new data
        file = open("C:\_PythonClass\ToDo.txt","w")
        #pull values from the dictionary and turn them into a list; save to file
        for x in tblData:
            x.values()
            this_list = list(x.values())
            file.write(this_list[0] + "," + this_list[1])
        file.close()
        
        
#load the current data in the text file   
x = ToDoList()
x.LoadData()
    
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
        x = ToDoList()
        x.ShowCurrentData()
        continue
    # Step 4 - Add a new item to the list/Table
    elif(strChoice == '2'):
        x = ToDoList()
        x.AddItem()
        continue
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        x = ToDoList()
        x.RemoveItem()
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        x = ToDoList()
        x.SaveData()
        continue
    elif (strChoice == '5'):
        break #and Exit the program    
