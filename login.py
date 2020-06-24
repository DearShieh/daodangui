# import os, sys
#
# sys.path.append(os.getcwd())
# sys.path.append("C:/Users/liufeifei/Desktop/daodangui")
import requests
import json
from data.get_data import GetData
from common.get_keyword import GetKeyword
from common.operation_excel import OperationExcel
from common.operation_json import OperationJson
import data.data_config


# 1.请求地址
# url = "https://ddg.mmvww.com/s/account/partner/login"
# data = {"phone":"18328207604","code":"0000"}
# res = requests.post(url=url,data=data,verify = False)
# print(res)

class Login:
    def __init__(self):
        self.data = GetData()

    def test_login(self,row=1):
        url = self.data.get_url(row)
        method = GetData().get_method(row)
        data = GetData().get_data_for_json(row)
        print(url,method,data)


        res = requests.post(url=url, data=data)
        print(json.dumps(res.json(),indent=2,ensure_ascii=False))
        # print(GetKeyword.format_response(res))
        return res

#
if __name__ == '__main__':
    b = Login()
    print(b.test_login())


# response = requests.request(url=url, method=method)
# 2.请求参数
        # application/x-www-form-urlencoded格式：
# headers = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTI1MzU0MTksInRpbWVzdGVtcCI6MTU5MTkzMDYxOTMzOCwidXNlciI6eyJ1c2VySWQiOjM5NCwidXNlclR5cGUiOjgsInVzZXJOYW1lIjpudWxsLCJwaG9uZSI6bnVsbCwiZXh0IjpudWxsfX0.9MTzvede666MBrbaX7azEPmfXYB5XUyWLUNP7N62wwA"}
        # from-data格式：  需要安装：pip install requests_toolbelt
        # 导包：from requests_toolbelt import MultipartEncoder
        # response = requests.post(url=url, dataconfig=dataconfig, headers = headers)
        # 组合headers     ~~~~

# 添加haeders:
# headers = {"ContentType" : "application/x-www-form-urlencoded"}
# response = requests.post(url=url, json=dataconfig, haeders=headers)

# 3.发送请求        application/x-www-form-urlencoded格式请求
# response = requests.get(url=url, headers=headers)
# https请求：
# response = requests.post(url=url, dataconfig=dataconfig,verify = False)
# json格式请求
# response = requests.post(url=url, json=dataconfig)

# 4.美化格式输出
# print(json.dumps(response.json(),indent=2,ensure_ascii=False))
# print(response.text)    # 文本格式显示
# print(response.json())    # json格式显示
# print(response.state_code)  # 显示响应状态码
# print(response.header)      # 显示响应头

# python与json之间的转换
# json.dumps()      # Python-->Json
# json.loads()