# importing the requests library
import requests

# api-endpoint
URL = "https://reqres.in/api/users?page={id}"

# location given here
#location = "delhi technological university"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'id':2}

# sending get request and saving the response as response object
r = requests.get(url = URL, params = PARAMS)
print(r.url)

# extracting data in json format
data = r.json()
print(data)



