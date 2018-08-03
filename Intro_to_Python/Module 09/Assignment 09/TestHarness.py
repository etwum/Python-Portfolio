# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 17:05:45 2017

@author: Emmanuel
"""

import DataProcessor, Person, Customers

print("Test the DataProcessor.File class")
objDP = DataProcessor.File()
objDP.FileName = "Test.txt"
objDP.TextData = "This is a test"
strMessage = objDP.SaveData()
print(strMessage)



print("\n Test the Person.Person class")
objP = Person.Person()
objP.fullname = "Bob","Smith"
print(objP.ToString())

print("\n Test the Employees.Employee class")
objE = Customers.Customer()
objE.customerinfo = 1,"Bob","Smith"
print(objE.ToString())


print("\n Test the Customer.CustomerList class")
objEL = Customers.CustomerList()
    
try:
    objEL.AddCustomer(objE)
    print("Trying the correct object type")
    print(objEL.ToString())
except:
    print("This should work")
