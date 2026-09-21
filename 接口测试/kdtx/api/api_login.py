import requests
from config import Base_Url, Headers, Headers_Json


class ApiLogin:
    """
    登录api类
    """

    def api_captchaImage(self):
        """
        获取验证码
        :return:
        """
        url=f'{Base_Url}/api/captchaImage'
        res= requests.get(url,headers=Headers)
        return res

    def api_login_method(self,uuid, username='admin', password='HM_2023_test', code=2):
        """
        登录
        :param username: 用户名
        :param password: 用户密码
        :param code: 验证码
        :param uuid: 唯一标识（获取验证码接口返回）
        :return:
        """
        url=f'{Base_Url}/api/login'
        data={"username":username,"password":password,"code":code,"uuid":uuid}
        res=requests.post(url,headers=Headers_Json,json=data)
        return res

# if __name__ == '__main__':
#     login = ApiLogin()
#     res1=login.api_captchaImage()
#     uuid= res1.json().get('uuid')
#     res2=login.api_login_method(uuid=uuid)
#     print(res2.json())