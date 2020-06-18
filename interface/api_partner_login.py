import os, sys

sys.path.append(os.getcwd())
from common.send_method import SendMethod
from common.get_keyword import GetKeyword
from data.get_data import GetData


class PartnerLogin:
    def __init__(self):
        self.url = GetData().get_url(1)
        self.method = GetData().get_method(1)
        self.data = GetData().get_data_for_json(1)

    def login(self):
        '''
            单接口测试
        '''
        # url = self.url.get_url(1)
        # method = self.method.get_method(1)
        # data = self.data.get_data_for_json(1)
        # print(self.method, self.url, self.data)
        res = SendMethod.send_method(self.method, self.url, data=self.data)
        return res

    # 获取返回的token
    def get_token(self):
        '''
            关联接口测试准备
        '''
        res = self.login()
        token = GetKeyword.get_value_by_keyword(res, "token")
        return token

# if __name__ == '__main__':
#     a = PartnerLogin()
#     a.login()