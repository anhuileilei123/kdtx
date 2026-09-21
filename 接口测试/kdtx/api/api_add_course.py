import requests
from config import Base_Url, Headers_Json

class AddCourse:
    """
    添加课程模块类
    """
    def api_add_course_method(self, token, name, subject, price, applicablePerson, info=None):
        """
        添加课程方法
        :param token: 登录接口返回的token
        :param name: 课程名称
        :param subject: 课程学科
        :param price: 课程价格
        :param applicablePerson: 适用人群
        :param info: 课程介绍（选填）
        :return:
        """
        url=f'{Base_Url}/api/clues/course'
        data={"name":name,"subject":subject,"price":price,"applicablePerson":applicablePerson,"info":info}
        headers={**Headers_Json,'Authorization':f'Bearer {token}'}
        res=requests.post(url,headers=headers,json=data)
        return res
    def api_query_course_method(self, token,name=None):
        """
        根据名字查找课程
        :param token:
        :param name:
        :return:
        """
        url = f'{Base_Url}/api/clues/course/list'
        headers = {**Headers_Json, 'Authorization': f'Bearer {token}'}
        params={"name": name}
        res=requests.get(url=url,headers=headers,params=params)
        return res