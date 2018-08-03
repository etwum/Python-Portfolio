

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
        strInventoryValue = input("Please enter the estimated value of the item: " )
        #Create a tuple for the household item and it's value
        tplInventory = (strInventoryItem, strInventoryValue)
        tplTable = ((tplInventory),)
        
        #Ask user if he or she would like to enter more items
        strInputMoreItems = input("Would you like to input more items? input (yes or no): ")
        
        #User inputs yes then enter another household item and the value
        if(strInputMoreItems.lower() == "yes"):
            
            strNewInventory = input("Please enter another household item: ")
            strNewInventoryValue = input("Please enter the items estimated value: ")
            #Tuple for new item input
            tplNewItems = ((strNewInventory, strNewInventoryValue),)
            #add first item/value with second item/value into a tuple
            tplTable += (tplNewItems)
           
        else:
            #Save first item in the inventory list or not
            SaveItem = input("Would you like to save this item in the inventory list? input(yes or no): ")
            if(SaveItem.lower() == "yes"):   
                #Writes the inputs to the text file
        
                file.write(str(tplTable))
                file.close()
                continue

            else:
                #Saves closes and saves file
                file.close()
                continue
    #Ask the user if he or she wants to after inputting the second item and value     
    SaveItem = input("Would you like to save these items in the inventory list? input(yes or no): ")
    if(SaveItem.lower() == "yes"):   
        #Writes the inputs to the text file
        file.write(str(tplTable))

    else:
        #Saves closes and saves file   
        file.close()  
#Saves closes and saves file        
file.close()

