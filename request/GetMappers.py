'''
Created on 27-Mar-2021

@author: Cabin
'''
import requests
response = requests.get("http://localhost:8080/SpringRestExample-1.0.0-BUILD-SNAPSHOT/display")
print(response.json())