import requests
from config import Base_Url, Headers, Headers_Json


class ApiLogin:
    """
    登录api类
    """

    def api_captcha_image(self):
        """
        获取验证码
        先调用该接口拿到 uuid + 验证码图片，uuid 需要传给登录接口做关联校验
        :return: requests响应对象（json中含 uuid / img 等字段）
        """
        url = f'{Base_Url}/api/captchaImage'
        res = requests.get(url, headers=Headers)
        return res

    def api_login_method(self, username=None, password=None, code=None, uuid=None):
        """
        登录
        注意：uuid 是验证码接口返回的唯一标识，必须由测试脚本先调用
        api_captcha_image() 获取后传入，不能在api层写死或自动生成
        :param username: 用户名（必填，缺失用例可不传）
        :param password: 用户密码（必填，缺失用例可不传）
        :param code: 验证码（必填，缺失用例可不传）
        :param uuid: 验证码唯一标识（必填，由获取验证码接口返回；缺失用例可不传）
        :return: requests响应对象
        """
        url = f'{Base_Url}/api/login'
        data = {"username": username, "password": password, "code": code, "uuid": uuid}
        # 必填字段缺失用例：未传入的参数不放进请求体，真实模拟"字段缺失"而非传null
        data = {k: v for k, v in data.items() if v is not None}
        res = requests.post(url, headers=Headers_Json, json=data)
        return res
