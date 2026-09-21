import pytest

from api.api_login import ApiLogin


@pytest.fixture(scope='class')
def get_token():
    """
    类级别fixture：登录获取token
    :return:
    """
    login = ApiLogin()
    res_captcha = login.api_captcha_image()
    token_uuid = res_captcha.json().get('uuid')
    res_login = login.api_login_method(username='admin', password='HM_2023_test', code='2', uuid=token_uuid)
    yield res_login.json().get('token')
