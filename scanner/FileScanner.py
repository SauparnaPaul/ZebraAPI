'''
Created on 26-Mar-2021

@author: Cabin
'''
import os, re
    
def splitSlash(string):
    li = list(string.split("/"))
    return li

def isMapping(line,path):
    if(line.find('@RequestMapping')!=-1):
        return contextUri(line)
    else:
        return None
        
def contextUri(line):
    return re.findall(r"/\w+",line)[0]     
    
def readFileForController(path,filename=""):
    listOfURIs=[]
    isController=False
    with open(path, 'r') as file:
        for line in file:
            if (line.find('@Controller')!=-1):
                #print("Found Controller : "+path.split("\\")[-1] )
                isController=True
            if(isController and isMapping(line, path) is not None):
                listOfURIs.append(isMapping(line, path))
            
        file.close()
        return listOfURIs