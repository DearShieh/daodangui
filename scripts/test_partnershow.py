import unittest
import os, sys

sys.path.append(os.getcwd())
from interface.api_partner_login import PartnerLogin
from interface.api_partner_show import Partnershow
from common.get_keyword import GetKeyword
from data.get_data import GetData


class Test_PartnerShow(unittest.TestCase):
    def setUp(self):
        self.expect_data = GetData()
        self.login = PartnerLogin()
        self.show = Partnershow()

    def test_show(self):
        # data = {"phone": "18328207604", "code": "0000"}
        # token = "Bearer " + self.login.get_token(data)
        # print(token)
        # headers = {"Authorization": token}  # “token”不能加引号！！！！
        res = self.show.show()
        print(GetKeyword.format_response(res))

        # Assertion:
        expect_data = self.expect_data.get_expect_data(2)
        code = str(GetKeyword.get_value_by_keyword(res, "code"))
        # res =str(res)
        # print(type(expect_data), type(res))
        try:
            self.assertIn(code, expect_data)
            self.expect_data.write_result(2, 'Pass')
            print('Pass')
        except AssertionError:
            self.expect_data.write_result(2, res)
            raise print('Fail')


        # code = GetKeyword.get_value_by_keyword(res, "code")
        # self.assertEqual(code, 1)

# if __name__ == '__main__':
#     unittest.main()
