import json
# import dataconfig

# fp = open('../dataconfig/partner_login.json')
# dataconfig = json.load(fp)
# print(dataconfig['partner_login'])


class OperationJson:
    def __init__(self):
        self.data = self.read_data
        # 读取json文件
    @property
    def read_data(self):
        with open('./dataconfig/partner_login.json') as fp:
            data = json.load(fp)
            return data
        # 根据关键字获取数据
    def get_data(self,id):
        return self.data[id]

# if __name__ == '__main__':
#     opjson = OperationJson()
#     print(opjson.get_data('partner_login'))