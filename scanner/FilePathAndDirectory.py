'''
Created on 27-Mar-2021

@author: Cabin
'''
import os
from scanner.FileScanner import readFileForController


def isEmptyList(list):
    if not list:
        return True
    else:
        return False
    
    
def fileScanner(location="",):
    files_in_dir = []
    listOfHttpEndpoints= []
    
    for r, d, f in os.walk(location):
       for item in f:
          if '.java' in item:
            path=os.path.join(r, item)
            files_in_dir.append(path)
            list=readFileForController(path)
            if(not isEmptyList(list)):
                listOfHttpEndpoints.append(list)
    return listOfHttpEndpoints
    #for item in files_in_dir:
    #  print("file in dir: ", item)