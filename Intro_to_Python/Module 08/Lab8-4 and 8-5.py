# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:09:32 2017

@author: Emmanuel
"""

#Lab 8-4
#--- Make the class ---
class Person(object):
    """ Base Class for Personal data """
   
    #--Fields--
    #FirstName = ""
    __Counter = 0 #Hey Devs, please consider this a private field!

    #--Constructor--
    def __init__(self, FirstName = ""):
        #Attributes
        self.__FirstName = FirstName # Private Attribute
        Person.__SetObjectCount() # Private Method
        
    def __str__(self):
        rep = "Here's the first name: " + self.__FirstName 
        return rep
    
    #--Properties--    
    #FirstName    
    @property #getter(accessor) 
    def FirstName(self):
        return self.__FirstName
    
    @FirstName.setter #(mutator)
    def FirstName(self, Value):
        self.__FirstName = Value
#--Methods--

    def ToString(self):
        """Explictly returns field data"""
        return self.__FirstName
    
    @staticmethod
    def GetObjectCount(): # You do not need the self keyword
        return Person.__Counter

    @staticmethod
    def __SetObjectCount(): # This is a private and static method
        Person.__Counter += 1 
    
# --- Use the class ----
# by making an object!
objP1 = Person("Bob")
print(Person.GetObjectCount())

objP2 = Person()
objP2.FirstName = "Sue" 
print(Person.GetObjectCount())

print(objP1)
print(objP2)

#Lab 8-5 - Inheritance (Inherit Lab 8-4)
class Employee(Person):
    
    count = 0
    
    def __init__(self, FirstName="", ID = ""):
        #Attributes
        self.__ID = ID
        super().__init__(FirstName) #Using the first name attribute from the Parent Class
        
        Employee.count += 1
        
        
    def __str__(self):
        rep = "Here's the ID: {0} and first name: {1} ".format(self.__ID, self.__FirstName)  #can change to super().FirstName
        return rep
    
    @property #getter(accessor) 
    def FirstName(self):
        return 'ID:{0} First Name:{1}'.format(self.__ID, self.__FirstName)     #can change to super().FirstName
    
    @FirstName.setter #(mutator)
    def FirstName(self, Value):
        first, ID = Value
        self.__FirstName = first
        self.__ID = ID
        
    def employee_name(self):
        return super().FirstName + " " + str(self.__ID)

       
emp1 = Employee("Bob",1)
print(emp1.employee_name())

emp1.FirstName = ("China",1)
print(emp1)

print(emp1.FirstName)
print(Employee.count)



    


