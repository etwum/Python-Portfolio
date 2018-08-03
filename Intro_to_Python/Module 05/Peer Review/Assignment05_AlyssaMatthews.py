# -------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   AlyssaMatthews, 10/27/2017, Added code to complete assignment 5
# -------------------------------------------------#

# -- Data --#
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection
# strNewTask = A new task entry provided by the user
# strNewPriority = A new priority entry provided by the user
# strTask = A string to use when searching for an existing task
# boolTaskFound = Boolean flag for noting when a task exists in the list

# -- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

# -- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
# -------------------------------

strData = ""
dicRow = {}
lstTable = []

# Step 1 - Load data from a file
objFile = open("ToDo.txt", "r")
for line in objFile:
    strData = line
    dicRow = {"task": (strData.split(",")[0]).strip(), "priority": (strData.split(",")[1]).strip()}
    lstTable.append(dicRow)
objFile.close()


# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item
    3) Remove an existing item
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()  # adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow["task"] + "," + dicRow["priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strNewTask = input("Enter a task: ")
        strNewPriority = input("Enter the task's priority: ")
        dicRow = {"task": strNewTask.title(), "priority": strNewPriority.lower()}
        lstTable.append(dicRow)
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice == '3'):
        strTask = input("Enter the task you wish to remove: ")
        boolTaskFound = False
        if len(lstTable):
            for dicRow in lstTable:
                if strTask.title() in dicRow["task"]:
                    lstTable.remove(dicRow)
                    boolTaskFound = True
                    print("The task", strTask.title(), "has been removed")
        if not boolTaskFound:
            print("Task not found")
        continue

    # Step 6 - Save tasks to the ToDo.txt file
    elif (strChoice == '4'):
        objFile = open("ToDo.txt", "w")
        if len(lstTable):
            for dicRow in lstTable:
                objFile.write(dicRow["task"] + "," + dicRow["priority"] + "\n")
            print("Data saved")
        else:
            print("No entries found")
        objFile.close()
        continue

    elif (strChoice == '5'):
        break  # and Exit the program

