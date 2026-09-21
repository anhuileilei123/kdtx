import json
import os

import pytest

from api.api_login import ApiLogin
from common.common_assert import CommonAssert

# 测试数据文件路径（data/login_data.json）
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'login_data.json')
with open(DATA_FILE, encoding='utf-8') as f:
    case_data = json.load(f)


def build_request(case, uuid):
    """
    构造登录请求体：将用例中的占位符 ${uuid} 替换为验证码接口实时返回的uuid
    :param case: 单条测试用例
    :param uuid: 验证码接口返回的唯一标识
    :return: 可直接发送的请求体dict
    """
    request = {}
    for k, v in case['request'].items():
        request[k] = uuid if v == '${uuid}' else v
    return request


class TestLogin:
    """
    登录模块测试用例层（数据驱动）
    测试数据来自 data/login_data.json，通过 @pytest.mark.parametrize 参数化执行
    """
    login = ApiLogin()

    # 提取用例描述作为参数化用例标题，报告中可读性更好
    case_ids = [case['case_id'] + '-' + case['case_name'] for case in case_data['cases']]

    @pytest.mark.parametrize('case', case_data['cases'], ids=case_ids)
    def test_login(self, case):
        """
        登录接口数据驱动测试
        :param case: 单条登录测试用例（来自login_data.json）
        :return:
        """
        # 前置：调用验证码接口获取uuid（uuid由外部获取后传入登录接口）
        res_captcha = self.login.api_captcha_image()
        uuid = res_captcha.json().get('uuid')

        # 组装请求体并执行登录
        payload = build_request(case, uuid)
        res = self.login.api_login_method(**payload)
        print(f'{case["case_id"]}: {res.json()}')

        # 断言：HTTP状态码 + 业务code + msg + 成功时token非空
        expect = case['expect']
        CommonAssert.assert_common(res,
                                   status_code=expect['status_code'],
                                   code=expect['code'],
                                   msg=expect['msg'])
        if expect['token_not_null']:
            assert res.json().get('token'), '登录成功场景必须返回token'
        else:
            assert not res.json().get('token'), '登录失败场景不应返回token'

    def test_login_success(self):
        """
        登录成功场景（保留原正向用例，走通用断言）
        :return:
        """
        # 获取验证码
        res_captcha = self.login.api_captcha_image()
        uuid = res_captcha.json().get('uuid')
        # 登录（uuid由外部传入）
        res = self.login.api_login_method(username='admin', password='HM_2023_test', code='2', uuid=uuid)
        print(f'登录成功: {res.json()}')
        # 断言
        CommonAssert.assert_common(res)
        assert res.json().get('token')
