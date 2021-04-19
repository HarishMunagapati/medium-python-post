import config

import requests

url = "https://api.medium.com/v1/me"

userid=config.user_id

payload={}
headers = {
  'Authorization': "Bearer userid"
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
