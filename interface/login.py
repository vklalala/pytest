import requests
import json

headers = {"Content-Type": "application/json;charset=utf8"}
url = "http://120.77.215.105/prod-api/auth/login"
_data = {
    "username": "admin",
    "password": "admin123"
}
res = requests.post(url=url, headers=headers, json=_data).text
access_token=res.code
print(res)