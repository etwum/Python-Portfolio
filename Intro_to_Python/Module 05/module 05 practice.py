# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:50:44 2017

@author: Emmanuel
"""

list = ["a", "b", "c", "d"]
list.append("e")
list2 = [5, 8, 11]
#list.extend(list2)
#print(list)



list4 =[list, list2]
print(list4)

list3 = ['hello', 'moto']

list4.insert(0,list3)

print(list4)
    
#Writing a list to a text file
file = open("List3.txt", "a")
list1 = [1, "Bob Smith", "BSmith@hotmail.com"]
list2 = [2, "Sue Jones", "SueJ@yahoo.com"]
list3 = [3, "Joe James", "JoeJames@gmail.com"]
tableOfList = [list1, list2, list3]
id = 3


while(True):
    userinput1 = input("Please enter your name: ")
    userinput2 = input("Please enter your email: ")
    id += 1
    list4 = [id, userinput1, userinput2]
    tableOfList.append(list4)
    userinput3 = input("Would you like to continue inputting items? (Y/N) ")
    if(userinput3.lower() == 'y'):
        continue
    else:
        userinput4 = input("Would you like to save? (Y/N) ")
        if(userinput4.lower() == 'y'):
            file.write(str(tableOfList))
            file.close()
            print("Saving")
        else:
            print("Not Saved!")
    userinput5 = input("Input 'exit' to close the program: ")
    if(userinput5.lower() == 'exit'): break
file.close()

#Dictionary

dicRow1 = {"ID":1, "Name":"Bob Smith", "Email":"BSmith@hotmail.com"}

for MyKey, MyValue in dicRow1.items():
    print(MyKey, "=", MyValue)


print(dicRow1.values())
print(dicRow1.keys())


#writing a dictionary to a text file
file = open("Dictionary.txt", "a")
dic1 = {"ID":1, "Name":"Bob Smith", "Email":"BSmith@hotmail.com"}
dic2 = {"ID":2, "Name":"Sue Jones", "Email":"SueJ@yahoo.com"}
dic3 = {"ID":3, "Name":"Joe James", "Email":"JoeJames@gmail.com"}
tableOfDicts = [dic1, dic2, dic3]
id = 3


while(True):
    userinput1 = input("Please enter your name: ")
    userinput2 = input("Please enter your email: ")
    id += 1
    dic4 = {"ID":id, "Name":userinput1, "Email":userinput2}
    tableOfDicts.append(dic4)
    userinput3 = input("Would you like to continue inputting items? (Y/N) ")
    if(userinput3.lower() == 'y'):
        continue
    else:
      userinput4 = input("Would you like to save? (Y/N) ")
      if(userinput4.lower() == 'y'):
          file.write(str(tableOfDicts))
          file.close()
          print("Saving")
      else:
          print("Not Saved!")
    userinput5 = input("Input 'exit' to close the program: ")
    if(userinput5.lower() == 'exit'): break
file.close()


#Structured Error Handling
try:
    x = 5
    y = 0
    print(x/y)
except:
    print("An error occurred!")
    
    
    
#Script Templates  - Data, Processing, Presentation (Input/Output)


#****Data****
#declare variables and CONSTANTS
fltN1 = 0.0
fltN2 = 0.0


#***Processing***
#perform task
def DivideValues():
    return (fltN1/fltN2)


#***Presentation (Input/Output)****
#get user input
fltN1 = float(input("Please enter a number: "))
fltN2 = float(input("Please enter another number: "))

#send program output
print(DivideValues())





