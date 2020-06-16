import requests
import json
# 1.请求地址
url = "http://192.168.0.123:8082/userPartner/show"

# 2.请求参数
        # application/x-www-form-urlencoded格式：
headers = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTI1MzU0MTksInRpbWVzdGVtcCI6MTU5MTkzMDYxOTMzOCwidXNlciI6eyJ1c2VySWQiOjM5NCwidXNlclR5cGUiOjgsInVzZXJOYW1lIjpudWxsLCJwaG9uZSI6bnVsbCwiZXh0IjpudWxsfX0.9MTzvede666MBrbaX7azEPmfXYB5XUyWLUNP7N62wwA"}
        # from-data格式：  需要安装：pip install requests_toolbelt
        # 导包：from requests_toolbelt import MultipartEncoder
        # response = requests.post(url=url, data=data, headers = headers)
        # 组合headers     ~~~~

# 添加haeders:
# headers = {"ContentType" : "application/x-www-form-urlencoded"}
# response = requests.post(url=url, json=data, haeders=headers)

# 3.发送请求        application/x-www-form-urlencoded格式请求
response = requests.get(url=url, headers=headers)
# https请求：
# response = requests.post(url=url, data=data,verify = False)
# json格式请求
# response = requests.post(url=url, json=data)

# 4.美化格式输出
print(json.dumps(response.json(),indent=2,ensure_ascii=False))
# print(response.text)    # 文本格式显示
# print(response.json())    # json格式显示
# print(response.state_code)  # 显示响应状态码
# print(response.header)      # 显示响应头

# python与json之间的转换
# json.dumps()      # Python-->Json
# json.loads()