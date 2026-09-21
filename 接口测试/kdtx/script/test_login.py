import pytest

from api.api_login import ApiLogin
from common.common_assert import CommonAssert


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
        CommonAssert.assert_common(res)
        assert res.json().get('token')
