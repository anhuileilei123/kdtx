"""
通用断言类
"""


class CommonAssert:
    """
    公共断言：接口通用字段校验
    """

    @staticmethod
    def assert_common(res, status_code=200, code=200, msg='操作成功'):
        """
        通用断言方法
        :param res: requests响应对象
        :param status_code: 期望的HTTP状态码
        :param code: 期望的业务code
        :param msg: 期望的业务msg
        :return:
        """
        assert res.status_code == status_code
        assert res.json().get('code') == code
        assert res.json().get('msg') == msg
