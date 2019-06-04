import json
import requests

url = 'https://reqres.in/api/{users}'
data = {'users': 'john'}
#headers = {'content-type': 'application/json'}

r = requests.post(url, data=data)

print(r.text)
