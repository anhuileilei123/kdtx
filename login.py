

import requests
import json
from tool import *
from config import *

url = Base_URL+"/api/login"
uuid=get_uuid()
json={
   "username": "admin",
   "password": "HM_2023_test",
   "code": "2",
   "uuid":uuid
}
"""payload = json.dumps({
   "username": "admin",
   "password": "HM_2023_test",
   "code": "2",
   "uuid":uuid
})"""
headers = {
   'Content-Type': 'application/json',
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                 '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, json=json)

print(response.text)