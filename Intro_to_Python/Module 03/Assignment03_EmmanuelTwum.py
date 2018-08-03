

#Opens the file if already created and appends the current data. Creates a new file if the file isnt created
file = open("HomeInventory.txt", "a")

#Start Loop
while(True):
    
    #User input for inventory item or end the loop
    strInventoryItem = input("Please enter a household item to store in the inventory list or type 'close' to exit: ")
    if(strInventoryItem.lower() == "close"):
        print("\nClosing Inventory File")
        break
    
    else:
        #User input for inventory item value
        strInventoryValue = input("Please enter the value of the item: " )
        
        #Writes the inputs to the text file and creates a new line
        file.write("Item: " + strInventoryItem.capitalize() + "  Value: " +"$" + strInventoryValue + "\n")
        
#Saves closes and saves file
file.close()