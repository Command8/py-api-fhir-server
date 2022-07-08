

from urllib import response
import requests
import json
from h11 import Response

payload = {"resourceType": "CapabilityStatement","name": "RestServer","status":"active"}

r = requests.get ('http://hapi.fhir.org/baseR4/metadata', params= payload)
#r = requests.get ('http://localhost:8080/fhir/metadata', params= payload)
r.status_code
print (r.status_code)


r.headers['content-type']
r.encoding

r.json

#print(r.text)


