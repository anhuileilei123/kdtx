import requests
from config import Base_Url

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
        res=requests.post(url,headers={'User-Agent':'Mozilla/5.0','Content-Type':'application/json','Authorization':f'Bearer {token}'},json=data)
        return res
