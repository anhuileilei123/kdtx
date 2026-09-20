"""
测试验证码功能
"""
import requests

from config import Base_URL

url = Base_URL + "/api/captchaImage"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


response = requests.get(url=url, headers=headers)

print("状态码:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))


response.raise_for_status()
print(response.json())



