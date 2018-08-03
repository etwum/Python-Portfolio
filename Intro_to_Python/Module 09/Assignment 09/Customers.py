#-------------------------------------------------#
# Title: Classes for Customer Data
# Dev:   Emmanuel Twum
# Date:  11/25/2017
#-------------------------------------------------#

import Person

if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


class Customer(Person.Person):
    """Customer data class"""
    def __init__(self, CustomerNumber = None, FirstName="", LastName=""):
        self.__CustomerNumber = CustomerNumber
        super().__init__(FirstName,LastName) #Using the first name and last names attributes from the Parent Class
        
        
    def __str__(self):
        rep = "Here's the Customer Number: {0}  first name: {1} last name {2}".format(self.__CustomerNumber, self.__FirstName, self.__LastName) 
        return rep
    
    @property #getter
    def customerinfo(self):
        return 'Customer Number:{0} First Name:{1} Last Name:{2}'.format(self.__CustomerNumber, self.__FirstName, self.__LastName)
    
    @customerinfo.setter #setter
    def customerinfo(self, Value):
        customernumber, first, last = Value
        self.__CustomerNumber = customernumber
        self.__FirstName = first
        self.__LastName = last
        
        
    def ToString(self):
        return str(self.__CustomerNumber) + "," + self.__FirstName + "," + self.__LastName
        



class CustomerList(object):
    """ Static class for holding a list of customer data """
    
    #--Fields--
    __lstCustomers = [] #list of customers


    #--Methods--      
    @staticmethod            
    def AddCustomer(Customer):
        print(Customer.__class__)
        if(str(Customer.__class__) == "<class 'Customers.Customer'>"):
            CustomerList.__lstCustomers.append(Customer)
            print(CustomerList.__lstCustomers)  
        else:
            raise Exception("Only Customer objects can be added to this list")
         
    
    @staticmethod           
    def ToString(): 
        """Explictly returns field data"""
        strData = ""
        for item in CustomerList.__lstCustomers:
            strData += str(item.CustomerNumber) + "," + item.FirstName + "," + item.LastName + "\n"
        return strData
    
    @staticmethod
    def __str__(): # This overrides the original method as well
        """Implictly returns field data"""
        strData = CustomerList.ToString
        return strData    

    
