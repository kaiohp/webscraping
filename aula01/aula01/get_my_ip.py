import json

import requests

url = "https://lumtest.com/myip.json"

response = requests.get(url)

if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))

else:
    print("erro")
