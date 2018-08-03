# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:49:52 2017

@author: Emmanuel
"""

#***********************Classes

#Example 1
class Customer(object):
    id = None                     #Data in a class is definedd as variables (called Fields)
    Name = None
    
    def ToString(self):
        return str(self.id) + "," + str(self.Name)
    
    
#Example 2
class Person(object):
    FirstName = ""
    
    def ToString(self):
        return self.FirstName
    
objP1 = Person()
objP1.FirstName = "Bob"

objP2 = Person()
objP2.FirstName = "Sue"


print(objP1.ToString())
print(objP2.ToString())


#**********************Standard Class Pattern

#class Person(object):
#-----------------------#
#Description:
#Developer Name:
#Date:
#ChangeLog: (When,Who,What)
#-----------------------#

    #---Fields (not needed)
    #---Constructor
        #---Attributes
    #---Properties
    #---Methods
    
#--End of lcass   


# Lab 8-1

class Person(object):
    FirstName = ""
    LastName = ""
    
    def ToString(self):
        return str(self.FirstName) + " " + str(self.LastName)
    
objP1 = Person()
objP1.FirstName = "Bob"
objP1.LastName = "Ross"

objP2 = Person()
objP2.FirstName = "Sue"
objP2.LastName = "Bird"


print(objP1.ToString())
print(objP2.ToString())
    

#*********************Constructor

class Person(object):
    FirstName = ""                    #Field
    
    def __init__(self,FirstName):     #Constructor
        self.FirstName = FirstName    #Attribute
        
    def ToString(self):
        return self.FirstName
    
objP1 = Person("Bob")          #Pass the First Name to the class Person

print(objP1.ToString())


#Lab 8-2
class Person(object):
    FirstName = ""                              #Field
    LastName = ""                               #Field
    
    def __init__(self,FirstName,LastName):      #Constructor
        self.FirstName = FirstName              #Attribute
        self.LastName = LastName                #Attribute
   
    def ToString(self):
        return str(self.FirstName) + " " + str(self.LastName)
    
objP1 = Person("Bob", "Ross")          #Pass the First and Last Name to the class Person

print(objP1.ToString())
    


#Private Field - Cant be set directly
class Person(object):
    FirstName = ""                              #Field
    LastName = ""                               #Field
    
    def __init__(self,FirstName,LastName):      #Constructor
        self.__FirstName = FirstName              #__FirstName means private
        self.__LastName = LastName                #__LastName means private
   
    def ToString(self):
        return str(self.__FirstName) + " " + str(self.__LastName)
    
objP1 = Person("Bob", "Ross")          #Pass the First and Last Name to the class Person

objP1.__FirstName = "John"    #Doesnt work since FirstName is private
objP1.__LastName = "Doe"      #Doesnt work since LastName is private

print(objP1.ToString())



#****Properties

class Person(object):
    """ Base Class for Personal data """
    #-------------------------------------#
    #Desc:  Holds Personal data
    #Dev:   RRoot 
    #Date:  12/12/2012
    #ChangeLog:(When,Who,What)
    #-------------------------------------#
    
    #--Fields--
    #FirstName = ""

    #--Constructor--
    def __init__(self,FirstName = ""):
        #Attributes
        self.__FirstName = FirstName
    
    #--Properties--Best practice
    #FirstName    
    @property  # (getter or accessor) 
    def FirstName(self):                #public #get data
        return self.__FirstName
    
    @FirstName.setter  # (setter or mutator)
    def FirstName(self, Value):         #public #set data
        self.__FirstName = Value 
 
    #--Methods--
    def ToString(self):
        return self.FirstName 
#--End of class--

# --- Use the class ----
# by making an object!
objP1 = Person("Bob")

objP2 = Person()
objP2.FirstName = "Sue" 

print(objP1.ToString())
print("-------------")
print(objP2.ToString())




#Getter/Setter Example
class Employee(object):
    
    def __init__(self,first="",last=""):
        self.__first = first
        self.__last = last
    
    @property                #gets first and last name from fullname.setter
    def email(self):
        return '{0}.{1}@gmail.com'.format(self.__first,self.__last)
    
    @property                #gets first and last name from fullname.setter
    def fullname(self):
        return '{0}.{1}'.format(self.__first,self.__last)
    
    @fullname.setter         #setter                #allows you to set the fullname and email getters
    def fullname(self,name):
        first, last = name
        self.__first = first
        self.__last = last
        
    
    
    
emp1 = Employee()

#emp1.fullname = 'Jim Smith'
#emp1.email = 'Tom Frew'

emp1.fullname = ('Seth','Twum')

#emp1.__first = 'John'  #cant change since __.first is private
#emp1.__last = 'Doe'    #cant change since __.last is private


print(emp1.email)
print(emp1.fullname)

    
    
    
    
    