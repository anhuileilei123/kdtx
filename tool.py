import requests
from config import Base_URL

# 创建全局 Session 对象，用于复用 TCP 连接和统一配置
session = requests.Session()

# 统一设置 headers，避免每个请求重复设置
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
})

def get_uuid():
    """
    获取验证码 UUID
    
    使用 Session 发送请求，自动复用连接和 headers 配置
    """
    url = f"{Base_URL}/api/captchaImage"
    
    # 原先代码：
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    #                   "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    # }
    # response = requests.get(url=url, headers=headers)
    
    # 优化后：使用 Session 自动携带 headers
    response = session.get(url=url)
    
    print(response.json().get("uuid"))
    return response.json()["uuid"]

def get_session():
    """
    返回全局 Session 对象
    供其他模块复用，实现连接和配置共享
    """
    return session