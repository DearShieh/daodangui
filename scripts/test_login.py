import os, sys
import unittest

sys.path.append(os.getcwd())
from interface.api_partner_login import PartnerLogin
from common.get_keyword import GetKeyword
# from common.is_contain import IsContain
from data.get_data import GetData

class Test_login(unittest.TestCase):
    def setUp(self):
        # self.contain = IsContain()
        self.expect_data = GetData()
        self.login = PartnerLogin()

    def test_login(self):
        # data = {"phone": "18328207604", "code": "0000"}
        res = self.login.login()
        print(GetKeyword.format_response(res))
        # print(GetKeyword.get_value_by_keyword(res, "token"))

    # Assertion：
        expect_data = self.expect_data.get_expect_data(1)
        # if self.contain.is_contain(expect_data, res):
        #     print('Pass')
        # else:
        #     print('False')

        # code = GetKeyword.get_value_by_keyword(res, "code")
        # self.assertEqual(code, 1)
        pickupPhone = GetKeyword.get_value_by_keyword(res["data"]["partner"], "pickupPhone")

        # print(pickupPhone, expect_data)
        # print("是什么：%s"%(type(pickupPhone)))
        try:
            self.assertEqual(pickupPhone, expect_data)
            self.expect_data.write_result(1, 'Pass')
            print('Pass')
        except AssertionError:
            self.expect_data.write_result(1, res)
            raise print('Fail')
        #     print('Pass')
        # else:
        #     print('False')
        # self.assertIn(pickupPhone, expect_data)
# if __name__ == '__main__':
#
#     unittest.main()
