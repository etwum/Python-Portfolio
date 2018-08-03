# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 19:08:45 2017

@author: Emmanuel
"""

decision = None
tplData = ()

while decision != "":
    itemName = input("Name of Household Item?: ")
    itemValue = float(input("Value of Household Item?: "))
    tplRow = (itemName, itemValue)
    tplData += (tplRow),
    decision = input("\nInput any key to continue or please press 'Enter' to exit ")

decision = input("\nInput any key to save your data! If not, please press 'Enter': ")
if decision is not "":
    inventoryFile = open("test2.txt", "a")
    for i in tplData:
        inventoryFile.write("Item Name: " + str(i[0]) + "\nItem Value: $" + str(i[1]) + "\n\n")
    inventoryFile.close()
    print("\nYour data has been saved. Hope to see you again soon!")
else:
    print("\nYour data was not saved. Goodbye!")
