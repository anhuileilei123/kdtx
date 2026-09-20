"""
测试验证码功能
"""
import requests
from config import Base_URL
from tool import get_session

# 原先代码：
# url = Base_URL + "/api/captchaImage"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
# response = requests.get(url=url, headers=headers)

# 优化后：
# 1. 使用全局 Session 对象，复用 TCP 连接和 headers 配置
# 2. 使用 f-string 拼接 URL，更简洁
url = f"{Base_URL}/api/captchaImage"
response = get_session().get(url=url)

print("状态码:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))

response.raise_for_status()
print(response.json())