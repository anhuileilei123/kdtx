import json
import os

import pytest

from api.api_add_course import AddCourse
from common.common_assert import CommonAssert

# 测试数据文件路径（data/add_course_data.json）
DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'add_course_data.json')
with open(DATA_FILE, encoding='utf-8') as f:
    case_data = json.load(f)


class TestAddCourse:
    """
    添加课程模块测试用例层（数据驱动）
    测试数据来自 data/add_course_data.json，通过 @pytest.mark.parametrize 参数化执行
    """
    add_course = AddCourse()

    # 提取用例描述作为参数化用例标题，报告中可读性更好
    case_ids = [case['case_id'] + '-' + case['case_name'] for case in case_data['cases']]

    @pytest.mark.parametrize('case', case_data['cases'], ids=case_ids)
    def test_add_course(self, get_token, case):
        """
        新增课程接口数据驱动测试
        :param get_token: 登录token（conftest.py中的公共fixture）
        :param case: 单条新增课程测试用例（来自add_course_data.json）
        :return:
        """
        # no_token为true时不携带token，模拟未登录场景
        token = None if case.get('no_token') else get_token
        res = self.add_course.api_add_course_method(token=token, **case['request'])
        print(f'{case["case_id"]}: {res.json()}')
        # 断言：HTTP状态码 + 业务code + msg
        expect = case['expect']
        CommonAssert.assert_common(res,
                                   status_code=expect['status_code'],
                                   code=expect['code'],
                                   msg=expect['msg'])

    def test_query_course_success(self, get_token):
        """
        查找课程成功
        :param get_token:
        :return:
        """
        res = TestAddCourse.add_course.api_query_course_method(token=get_token, name='测试开发提升课01')
        # 断言
        assert res.status_code == 200
        assert '成功' in res.json().get('msg')
        assert res.json().get('code') == 200
