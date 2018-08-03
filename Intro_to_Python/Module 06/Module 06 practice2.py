# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:15:57 2017

@author: Emmanuel
"""

#*****Overloading (Python version) - polymorphism

#data
v1 = None
v2 = None
lstData = None

#processing
def AddValues(value1 = None, value2 = None, value3 = None):
    lstResults = None
    if(value3 is None):
        decAnswer = value1 + value2
        lstResults = [decAnswer, value1, value2]
    else:
        decAnswer = value1 + value2 + value3
        lstResults = [decAnswer, value1, value2, value3]
    return lstResults

#presentation
lstData = AddValues(5,10)
print(lstData)

lstData = AddValues(5,10,15)
print(lstData)


#*****Global Variables

# -- data code --
# Note: Variables declared in the body of the script are called "Global"
v1 = 10
v2 = 5
decAnswer = None  # result of processing

#processing
def AddValues(val1, val2):
   global decAnswer # decAnswer now refers to the "global variable" 
   decAnswer = val1 + val2 

# presentation

AddValues(v1, v2)
print("The Sum of the values "
      + str(v1) + " and " + str(v2) + " is: " + str(decAnswer) ) 

#****Shadowing a Global Variable
#data
# Note: Variables declared in the body of the script are called "Global"
v1 = 10    
v2 = 5     
decAnswer = None  

print(globals())

#processing
def AddValues(value1, value2):
    answer = 0  # This is a "local variable!"
    answer = value1 + value2
    decAnswer = answer 
    # decAnswer does NOT refer to the "global variable, but instead
    # "shadows" it!

# --presentation (I/0) code--
# Call the function

AddValues(v1, v2)
print("The Sum of the values "
      + str(v1) + " and " + str(v2) + " is: " + str(decAnswer) )
# This prints out -- "The Sum of the values 10 and 5 is: None"



#****Function Document Headers

def AddValues(value1, value2):
     """ This function adds two values """
    return v1 + v2

def AddValues(value1, value2):
    """ 
    :Desc : This function adds two values 
    :param value1: the first number to add
    :param value2: the second number to add
    :type value1: decimal or int
    :type value2: decimal or int
    :return: returns a sum of two numbers
    :rtype: decimal or int
    """
    return value1 + value2

print(AddValues(4,5))


#****Classes and Methods

#Example 1 - using Static Method
#data
v1 = 10
v2 = 11

#processing
class DoMath(object):
    @staticmethod
    def AddValues(value1, value2):
        return value1 + value2
   
#presentation

this = DoMath.AddValues(v1,v2)

print(this)

#Example 2 - using Self Method
#data
v1 = 10
v2 = 11

#processing
class DoMath(object):
    def AddValues(self, value1, value2):
        self.value = value1 + value2
        
    def get_value(self):
        return self.value
#presentation
this = DoMath()
this.AddValues(v1,v2)

print(this.get_value())


#Example 3
class Customer(object):
    Id = None
    Name = None
    
    def ToString(self):
        return str(self.Id) + " " + str(self.Name)
    
objCustomer1 = Customer()
objCustomer1.Id = 1
objCustomer1.Name = "Bob Smith"

objCustomer2 = Customer()
objCustomer2.Id = 2
objCustomer2.Name = "Sarah Smith"

print(objCustomer1.ToString())
print(objCustomer2.ToString())


#****Lab 6-3

n1 = 10
n2 = 20

class MathProcessor(object):
    AddValues = n1 + n2
    SubtractValues = n1 - n2
    MultipleValues = n1 * n2
    DivideValues = n1/n2


x = MathProcessor()

print(x.AddValues)
print(x.SubtractValues)
print(x.MultipleValues)
print(x.DivideValues)




