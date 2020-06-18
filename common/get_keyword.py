"""
    封装
    返回值中获取对应的值
"""
import jsonpath
from common.send_method import SendMethod


class GetKeyword(SendMethod):
    @staticmethod
    def get_value_by_keyword(data, keyword):
        return jsonpath.jsonpath(data, f"$..{keyword}")[0]


# if __name__ == '__main__':
#     # dataconfig = SendMethod.format_response
#
# #     dataconfig = {
# #   "code": 1,
# #   "dataconfig": {
# #     "partner": {
# #       "pickupPhone": "18328207604",
# #       "addTime": "2020-06-01 15:02:52",
# #       "bankCard": "5110567891012457",
# #       "bankOpenName": "四川天府银行锦江区分行",
# #       "idCard": "513925199712124565",
# #       "bankName": "四川天府银行",
# #       "realUserName": "杨敏",
# #       "userPartnerId": 6,
# #       "pickupUserName": "fhuadshfjsa",
# #       "pickupAddress": "四川省成都市武侯区鼎晟国际",
# #       "userAccountId": 394,
# #       "pickupLongitude": 103.97756,
# #       "deposit": 1,
# #       "partnerType": 2,
# #       "settlementProportion": 20,
# #       "pickupLatitude": 30.621843,
# #       "pickupName": "杨敏取货点"
# #     },
# #     "customer": {
# #       "lastLoginTime": "2020-06-11 14:00:03",
# #       "addTime": "2020-06-01 15:02:52",
# #       "phone": "17884848589",
# #       "userAccountId": 394,
# #       "frozen": 0,
# #       "userType": 8,
# #       "account": "18328207604"
# #     },
# #     "token": "eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTIyNzUwMjksInRpbWVzdGVtcCI6MTU5MTY3MDIyOTc5OCwidXNlciI6eyJ1c2VySWQiOjM5NCwidXNlclR5cGUiOjgsInVzZXJOYW1lIjpudWxsLCJwaG9uZSI6bnVsbCwiZXh0IjpudWxsfX0.R7LIa0RMkvFq5zK2TzQGGDWt0EZHmOye8ojM0ohu8Pc"
# #   }
# # }
#
#     token = GetKeyword.get_value_by_keyword(SendMethod.format_response, "token")
#     print(token)
