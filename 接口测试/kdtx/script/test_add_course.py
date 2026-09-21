import pytest

from api.api_add_course import AddCourse
from api.api_login import ApiLogin


class TestAddCourse:
    """
    添加课程模块测试用例层
    """
    login = ApiLogin()
    add_course = AddCourse()

    @pytest.fixture(scope='class', autouse=True)
    def get_token(self):
        """
        类级别fixture：登录获取token
        :return:
        """
        res_captcha = self.login.api_captchaImage()
        token_uuid = res_captcha.json().get('uuid')
        res_login = self.login.api_login_method(uuid=token_uuid)
        yield res_login.json().get('token')

    def test_add_course_success(self, get_token):
        """
        添加课程成功
        :param get_token: 登录token
        :return:
        """
        res = self.add_course.api_add_course_method(token=get_token, name='测试开发提升课01', subject='6',
                                                    price=899, applicablePerson='2', info='测试开发提升课01')
        print(f'添加课程: {res.json()}')
        # 断言
        assert res.status_code == 200
        assert res.json().get('code') == 200
        assert res.json().get('msg') == '操作成功'
