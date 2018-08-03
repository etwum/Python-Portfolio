# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 10:56:48 2017

@author: Emmanuel
"""

  # -- Data --#
  

strUserFileName = ""    # name of user text file
strFileFound = True     # confirm file is found


# -- Processing --#

def GetUserFileName():
    try:
        # Provide instructions for the user and request the file name
        print("This program will save your favorite text file in binary format.")
        while (True):
            strFile = input("Please enter the base file name of your text file:")
            return(strFile)
    except Exception as e:
        print("Error: " + str(e))

def CheckUserFile(File):
    try:
        # read file and print contents on screen for user
        objFile = open(File, "r")
        print("Here is the contents of your text file:")
        print("###########################")
        objFile.seek(0)
        # print file contents on screen
        print(objFile.read())
        if (objFile != None):
            objFile.close()
        # return true since file is found
        return(True)
    except Exception as e:
        print("Error: " + str(e))
        # return false since file not found
        return(False)

def WritePickleFile(File):
    try:
        objTextFile = open(File + ".txt", "r")
        objTextFile.seek(0)
        strFileContents = (objTextFile.read())

        # Now we store the data with the pickle.dump method
        objFile = open(File + ".dat", "ab")
        pickle.dump(strFileContents, objFile)
        objFile.close()

        # And, we read the data back with the same pickle.load method
        objFile = open(File + ".dat", "rb")
        objFileData = pickle.load(objFile)  # Note that load() only load one row of data.
        objFile.close()

        print("Here is the contents of your new pickle file:")
        print("###########################")
        print(objFileData)

    except Exception as e:
        print("Error: " + str(e))


  # -- Presentation (Input/Output) --#

try:
    # show the user a description of the program
    # and request the name of a text file from user
    strUserFileName = GetUserFileName()
    # read the text file and show contents to user, returns false if file not found
    strFileFound = CheckUserFile(strUserFileName + ".txt")
    if (strFileFound == False):
        # if file is not found notify user and do not continue
        print("Sorry, the your file " + strUserFileName + ".txt was not found!")
    else:
        # file is found, write data to new pickle file
        # and show the user the contents
        WritePickleFile(strUserFileName)

except Exception as e:
    print("Python reported the following error: " + str(e))