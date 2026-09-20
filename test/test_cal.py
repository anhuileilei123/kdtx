import allure
import pytest

from demo.cal import *


class Test:
    """计算器功能测试"""

    @pytest.fixture(scope="class")
    def pre_cal(self):
        print("计算前-")
        yield
        print("计算后-")

    @allure.feature("计算器")
    @allure.story("加法")
    @allure.title("加法：10 + 20 = 30")
    def test_1_add(self, pre_cal):
        num1 = 10
        num2 = 20
        res = add(num1, num2)
        assert res == 30

    @allure.feature("计算器")
    @allure.story("减法")
    @allure.title("减法：10 - 20 = -10")
    def test_2_sub(self, pre_cal):
        num1 = 10
        num2 = 20
        res = sub(num1, num2)
        assert res == -10
