# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 18:16:48 2017

@author: Emmanuel
"""

tplTable = ()


while(True):
    tplRow = (input('Enter the item name: '), )
    tplRow += (input("Enter the item's estimated value: "),)
    tplTable += (tplRow,)
    strContinue = input('Would you like to enter another item? (Y/N)')
    if strContinue.lower() == 'n': break

strSave = input('Would you like to save? (Y/N)')
if strSave.lower() == 'y':
    file = open("Test.txt","a")
    for row in tplTable:
        file.write(str(row) + "\n")
    file.close()

