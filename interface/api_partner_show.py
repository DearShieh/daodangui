from common.send_method import SendMethod
from common.get_keyword import GetKeyword

class Partnershow:
    def __init__(self,method="get"):
        self.url = "http://192.168.0.123:8082/userPartner/show"
        self.method = method

    def show(self,headers):
        res = SendMethod.send_method(self.method, self.url,headers=headers)
        return res