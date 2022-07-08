import sys

from email import header
from wsgiref import headers
import requests
from urllib3 import Timeout
import get_fhir

class Gold(object):
   #print("Line 7")
    def __init__(self):
        self.url = "http://hapi.fhir.org/baseR4/metadata"
        #self.url = "http://localhost:8080/fhir/metadata"
        print(self.url)
        self.headers = {
            'Server': 'nginx/1.18.0 (Ubuntu)',
            'Content-Type': 'application/json',  #'html/text',
            'Content-Length': '176',
            'Connection': 'keep-alive'}        
   
    @property
        
    def get(self):
            try:
                r = requests.get(url=self.url) #, headers=self.headers, timeout=1)
                if r.status_code==200:
                    print (r.status_code)
                    return r
                else:
                    print("evaluated to None")
                    return None 
            except requests.exceptions.Timeout:

                return 'Bad Response'


   # obj = Gold()
    #print(obj.get)
        

        #pass
