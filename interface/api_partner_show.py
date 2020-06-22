from common.send_method import SendMethod
from common.get_keyword import GetKeyword
from interface.api_partner_login import PartnerLogin
from data.get_data import GetData

class Partnershow:
    def __init__(self):
        self.login = PartnerLogin()
        self.url = GetData().get_url(2)
        self.method = GetData().get_method(2)

    def show(self):
        token = "Bearer " + self.login.get_token()
        headers = {"Authorization": token}          # “token”不能加引号！！！！
        # print(self.url, self.method, headers)
        res = SendMethod.send_method(self.method, self.url, headers=headers)
        return res

# if __name__ == '__main__':
#     a = Partnershow()
#     a.show()