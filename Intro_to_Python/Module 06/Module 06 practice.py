# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:32:09 2017

@author: Emmanuel
"""

#*************Using Encapsulaton to perform abstraction

#Abstraction is one of 3 key principles of object oriented programming.
#Encapsulation is a mechanics you use to provide abstraction

#Example

#Data
fltN1 = 0.0
fltN2 = 0.0

#Processing
def DivideValues():
    print(fltN1/fltN2)
    
#Presentation - input/output
#input
fltN1 = float(input("Enter the first number: "))
fltN2 = float(input("Enter the second number: "))
#output
DivideValues()

#Encapsulated version

#Data
fltN1 = 0.0
fltN2 = 0.0

#Processing
def DivideValues():
    fltN1 = 0.0
    fltN2 = 0.0
    fltN1 = float(input("Enter the first number: "))
    fltN2 = float(input("Enter the second number: "))
    flt = (fltN1/fltN2)
    return flt

def ShowValue():  
    print(DivideValues())
    

ShowValue()


#*****************Passing Arguments to Parameters of a function

#Example1
def ProcessSomething(p1):  #p1 is the parameter
    print("I'm")
    print("processing data: " + p1)
    
ProcessSomething("bbb")  #bbb is the argument

#Example2
def ProcessSomething(p1):  #p1 is the parameter
    print("I'm")
    print("processing data: " + p1)
    
a1 = "bbb"
ProcessSomething(a1)  #bbb is the argument

#Example3


def AddValues(value1, value2):
    decAnswer = value1 + value2
    return decAnswer

c1 = 10
c2 = 20


def Answer():
    print(AddValues(c1, c2))

Answer()

#*************Lab 6-1/6-2

#Data
def DoMath():
    number1 = float(input("Enter a number: "))
    number2 = float(input("Enter a second number: "))
    divide = number1/number2
    sum = number1 + number2
    difference = number1 - number2
    product = number1 * number2
    
    return divide, sum, difference, product #returns the values in a tuple 
    #return [divide, sum, difference, product] #returns the values in a list

#Processing    
def ShowResults():
    x1, x2, x3, x4 = DoMath()
    print("Divided: ", x1)
    print("Sum: ", x2)
    print("Difference: ", x3)
    print("Product: ", x4)
    
    
#Presentation  
ShowResults()

    
#************Positional vs Named Arguments

#data
v1 = 0
v2 = 0
lstData = 0

#processing
def AddVals(val1, val2):
    decAnswer = val1 + val2
    lstResults = [decAnswer, val1, val2]
    return lstResults

#Presentation
lstData = AddVals(10, 5) #positional argument  or lstData = AddVals(val1 = 10, val2 = 5) #named argument
print("The Sum of the values " + str(lstData[1]) + " and " + str(lstData[2]) + " is " + str(lstData[0]))


#****Default Parameter Values
x1 = 0
x2 = 0
lstData2 = 0

#processing
def AddValss(values1 = 0, values2 = 0):  #set defaults to zero
    decAnswer = values1 + values2
    lstResult = [decAnswer, values1, values2]
    return lstResult

lstData2 = AddValss(10)
print(lstData2)

lstData2 = AddValss(values1 = 10)
print(lstData2)

lstData2 = AddValss(values2 = 5)
print(lstData2)






