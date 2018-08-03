#-------------------------------------------------#
# Title: Customer Data Application
# Dev:   Emmanuel Twum
# Date:  11/25/2017
# Desc: This application manages customer data
#-------------------------------------------------#

if __name__ == "__main__":
    import DataProcessor, Customers
else:
    raise Exception("This file was not created to be imported")

#-- Data --# 
objE = None #an Customer object
intCustomerNumber = 0 #Customber Number
strFirstName = "" #Customer first name
strLastName = "" #Customer last name
strInput = "" 

#-- Processing --#
#perform tasks
def ProcessCustomerData(CustomerNumber, FirstName, LastName):
    #Create Customer object
    try:
        objE = Customers.Customer()
        objE.CustomerNumber = CustomerNumber
        objE.FirstName = FirstName
        objE.LastName = LastName
        Customers.CustomerList.AddCustomer(objE)
    except Exception as e:
        print(e)

def SaveDataToFile():
    #Save data to file
    try:
        objF = DataProcessor.File()
        objF.FileName = "CustomerData.txt"
        objF.TextData = Customers.CustomerList.ToString()
        objF.SaveData()
    except Exception as e:
        print(e)
        
#-- Presentation (I/O) --#
        
#get user input for customer name and last name
strUserInput = ""
while(True): 
  strUserInput = input("Would you like to add Customer data? (y/n) ")
  if(strUserInput == "y"):
      
      intCustomerNumber += 1
      
      strFirstName = str(input("Enter a Customer First Name: "))
      
      strLastName = str(input("Enter a Customer Last Name: ") )                        
      
      ProcessCustomerData(intCustomerNumber, strFirstName, strLastName)
  else:
      break 

#Show current customer data
print("The Current Data is: ")
print("------------------------")
print(Customers.CustomerList.ToString())

#Ask user to whether or not to save the customer data to file
strInput = input("Would you like to save this data to file?(y/n) ")
if(strInput == "y"):
    SaveDataToFile()
    #send program output   
    print("data saved in file")
else:
    print("data was not saved")

print("This application has ended.")
