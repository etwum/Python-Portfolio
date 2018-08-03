#-------------------------------------------------#
# Title: Base class for customer data
# Dev:   Emmanuel Twum
# Date:  11/25/2017
#-------------------------------------------------#

if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


class Person(object):
    """ Base Class for customer data """
   

    #--Constructor--
    def __init__(self, FirstName = "", LastName = ""):
        #Attributes
        self.__FirstName = FirstName # Private Attribute
        self.__LastName = LastName   #Private Attribute
    
    #--Properties--    
   
    @property #getter
    def fullname(self):
        return self.__FirstName, self.__LastName
    
    @fullname.setter #setter
    def fullname(self, name):
        first, last = name
        self.__FirstName = first
        self.__LastName = last
        
    #--Methods--

    def ToString(self):
        """Explictly returns field data"""
        return self.__FirstName + " " + self.__LastName
    


    
