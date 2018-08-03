# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 10:25:31 2017

@author: Emmanuel
"""
if __name__ == "__main__":
    import DataProcessor
else:
    raise Exception("This file was not created to be imported")


file = DataProcessor.File()
file.FileName = "Test.txt"
file.TextData = "Hello World"
print(file.SaveData())

print(file.ToString())
