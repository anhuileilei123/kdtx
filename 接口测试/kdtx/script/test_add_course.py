import pytest

from api.api_add_course import AddCourse
from common.common_assert import CommonAssert


class TestAddCourse:
    """
    添加课程模块测试用例层
    """
    add_course = AddCourse()

    def test_add_course_success(self, get_token):
        """
        添加课程成功
        :param get_token: 登录token（conftest.py中的公共fixture）
        :return:
        """
        res = self.add_course.api_add_course_method(token=get_token, name='测试开发提升课01', subject='6',
                                                    price=899, applicablePerson='2', info='测试开发提升课01')
        print(f'添加课程: {res.json()}')
        # 断言
        CommonAssert.assert_common(res)

    def test_query_course_success(self,get_token):
        """
        查找课程成功
        :param get_token:
        :return:
        """
        res=TestAddCourse.add_course.api_query_course_method(token=get_token,name='测试开发提升课01')
        # 断言
        assert res.status_code==200
        assert '成功'in res.json().get('msg')
        assert res.json().get('code')==200
