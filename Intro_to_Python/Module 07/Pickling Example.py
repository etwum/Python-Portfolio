# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:30:58 2017

@author: Emmanuel
"""

#import pickle module
import pickle

#create dictionaries with shoe list
dicRow1 = {"Company":"Nike", "Shoe Name":"Air Pegasus 89", "Size":10.5, "Category":"Sneakers"}
dicRow2 = {"Company":"Nike", "Shoe Name":"Air Stab", "Size":11, "Category":"Sneakers"}
dicRow3 = {"Company":"Cole Haan", "Shoe Name":"ZeroGrand Driver", "Size": 10.5, "Category":"Casual"}

#write to a binary file
file = open("Shoes List.dat","wb")

#move contents of each dictionary to the file
pickle.dump(dicRow1,file)
pickle.dump(dicRow2,file)
pickle.dump(dicRow3,file)

#close and save the file
file.close()


#unpickle #check to make sure the dat file save correctly
import pickle

#read binary file
file = open("Shoes List.dat","rb")

#read each pickled item from the file in sequential order
dicRow1 = pickle.load(file)
dicRow2 = pickle.load(file)
dicRow3 = pickle.load(file)

#print each item
print(dicRow1)
print(dicRow2)
print(dicRow3)

#close the file
file.close()



