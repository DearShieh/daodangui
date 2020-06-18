"""
    封装接口的请求方式（接口文档 ）
"""
import requests
import json

class SendMethod:
    @staticmethod  # 静态方法不需要实例化，使用方式：类名.静态方法
    def send_method(method, url, params=None, headers=None, data=None):
        if method == "get" or method == "delete":
            response = requests.request(method=method, url=url, params=params, headers=headers)
        elif method == "post" or method == "put":
            response = requests.request(method=method, url=url, data=data)
        else:
            print("请求方式错误！")
            response = None
        if method == "delete":
            return response.status_code
        else:
            return response.json()

    @staticmethod
    def format_response(response):
        """
        格式化返回数据
        :param response: 返回数据
        :return:
        """
        return json.dumps(response, indent=2, ensure_ascii=False)


# if __name__ == '__main__':
#     url = "http://192.168.0.233:8082/account/partner/login"
#     method = "post"
#     dataconfig = {"phone": "18328207604", "code": "0000"}
#     res = SendMethod.send_method(method=method, url=url, dataconfig=dataconfig)
#     # print(res)
#     print(SendMethod.format_response(res))