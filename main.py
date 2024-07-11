import requests

url = 'https://randomuser.me/api/'

response = requests.get(url)
# print status code
print(response.status_code)
# print type of response
print(type(response))