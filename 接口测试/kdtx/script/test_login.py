import pytest

from api.api_login import ApiLogin


class TestLogin:
    """
    登录模块测试用例层
    """
    login = ApiLogin()

    def test_login_success(self):
        """
        登录成功
        :return:
        """
        # 获取验证码
        res_captcha = self.login.api_captchaImage()
        uuid = res_captcha.json().get('uuid')
        # 登录
        res = self.login.api_login_method(uuid=uuid)
        print(f'登录成功: {res.json()}')
        # 断言
        assert res.status_code == 200
        assert res.json().get('code') == 200
        assert res.json().get('msg') == '操作成功'
        assert res.json().get('token')
