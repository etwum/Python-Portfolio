# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 14:17:24 2017

@author: Emmanuel
"""

#Data
objFile = None #File Handle
strUserInput = None #A string which holds user input


#Processing
class ProcessData(object):

    @staticmethod
    def WriteProductUserInput(File):
      try:
        print("Type in a Product Id, Name, and Price you want to add to the file")
        print("(Enter 'Exit' to quit!)")
        while(True):
          strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
          if(strUserInput.lower() == "exit"): break
          else: File.write(strUserInput + "\n")
      except Exception as e:
        print("Error: " + str(e))
   
    @staticmethod
    def ReadAllFileData(File, Message="Contents of File"):
      try:
        print(Message)
        File.seek(0)
        print(File.read())
      except Exception as e:
        print("Error: " + str(e))
 

#I/O
try:
  objFile = open("Products.txt", "r+")
  ProcessData.ReadAllFileData(objFile, "Here is the current data:")
  ProcessData.WriteProductUserInput(objFile)
  ProcessData.ReadAllFileData(objFile, "\nHere is the data that was saved:")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(objFile != None):objFile.close()