import requests


url = 'https://randomuser.me/api/'

response = requests.get(url)

# Get full name 
# Get email
# Get phone number
# Get address
data = response.json()
print(data['results'][0]['name']['first'])

    


