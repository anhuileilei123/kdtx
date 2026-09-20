"""
登录功能模块
"""
import requests
import json
from tool import *
from config import *

def login(username="admin", password="HM_2023_test", code="2"):
    """
    执行登录操作
    
    使用 Session 发送请求，与获取 UUID 共享 TCP 连接和 headers 配置
    
    Args:
        username: 用户名，默认为 admin
        password: 密码，默认为 HM_2023_test
        code: 验证码，默认为 "2"
    
    Returns:
        response: 响应对象
    """
    # 原先代码：
    # url = Base_URL+"/api/login"
    # uuid=get_uuid()
    # json={
    #    "username": "admin",
    #    "password": "HM_2023_test",
    #    "code": "2",
    #    "uuid":uuid
    # }
    # headers = {
    #    'Content-Type': 'application/json',
    #    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    #                  '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    # }
    # response = requests.request("POST", url, headers=headers, json=json)
    
    # 优化后：
    # 1. 使用 f-string 拼接 URL
    # 2. 复用全局 Session，自动携带 headers，实现连接复用
    url = f"{Base_URL}/api/login"
    uuid = get_uuid()  # 使用 Session 获取 UUID，共享连接
    
    json_data = {
       "username": username,
       "password": password,
       "code": code,
       "uuid": uuid
    }
    
    # 使用 Session 发送 POST 请求，自动携带 headers
    response = get_session().post(url, json=json_data)
    
    return response

# 执行登录并打印响应结果
if __name__ == "__main__":
    response = login()
    print(response.text)