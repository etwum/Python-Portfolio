#-------------------------------------------------#
# Title: Method to save customer data
# Dev:   Emmanuel Twum
# Date:  11/25/2017
#-------------------------------------------------#
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

class File(object):
    
    def __init__(self, FileName = "SavedData.txt", TextData = ""):
        #Attributes
        self.FileName = FileName
        self.TextData = TextData
 
    
    def SaveData(self):
        #save data to fle
        try:
            objFile = open(self.FileName, "a")
            objFile.write(self.TextData)
            objFile.close()   
        except Exception as e:
            print("Python reported the following error: " + str(e))
        return "Data Saved"
