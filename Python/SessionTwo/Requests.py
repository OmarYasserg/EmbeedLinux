# import requests

# r = requests.get( url = 'https://api.coindesk.com/v1/bpi/currentprice.jsonpip')

# print(r.json())

import requests
 
# Making a get request
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
 
# print response
print(response._content)
 
# print json content
# print(dir(response.json))