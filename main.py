import requests

url = 'https://randomuser.me/api'
for i in range(5):
    response = requests.get(url)
    print(response.status_code)