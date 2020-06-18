import os, sys
import unittest

sys.path.append(os.getcwd())
from interface.api_partner_login import PartnerLogin
from common.get_keyword import GetKeyword


class Testlogin(unittest.TestCase):
    def setUp(self):
        self.login = PartnerLogin()

    def test_login(self):
        data = {"phone": "18328207604", "code": "0000"}
        res = self.login.login(data)
        # print(GetKeyword.format_response(res))
        # print(GetKeyword.get_value_by_keyword(res, "token"))

        code = GetKeyword.get_value_by_keyword(res, "code")
        self.assertEqual(code, 1)
#
# if __name__ == '__main__':
#     unittest.main()
