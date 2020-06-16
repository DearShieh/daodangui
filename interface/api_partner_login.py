import os, sys

sys.path.append(os.getcwd())
from common.send_method import SendMethod
from common.get_keyword import GetKeyword


class PartnerLogin:
    def __init__(self, method="post"):
        self.url = "http://192.168.0.123:8082/account/partner/login"
        self.method = method

    def login(self, data):
        '''
            单接口测试
        '''
        res = SendMethod.send_method(self.method, self.url, data=data)
        return res

    # 获取返回的token
    def get_token(self, data):
        '''
            关联接口测试准备
        '''
        res = self.login(data)
        token = GetKeyword.get_value_by_keyword(res, "token")
        return token
