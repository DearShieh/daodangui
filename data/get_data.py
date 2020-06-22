import os, sys

sys.path.append(os.getcwd())
from common.operation_excel import OperationExcel
from common.operation_json import OperationJson
import data.data_config


class GetData:
    def __init__(self):
        self.excel = OperationExcel()
        self.json = OperationJson()
        self.data = data.data_config

    def get_case_lines(self):
        return self.excel.get_lines()

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = self.data.get_run()
        run = self.excel.get_cell_value(row, col)
        if run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求方式
    def get_method(self, row):
        col = self.data.get_method()
        return self.excel.get_cell_value(row, col)

    # 获取url
    def get_url(self, row):
        col = self.data.get_url()
        return self.excel.get_cell_value(row, col)

    # 是否需要headers
    def is_headers(self, row):
        col = self.data.get_headers()
        headers = self.excel.get_cell_value(row, col)
        if headers == 'no':
            return None
        else:
            return headers

    # 请求参数
    def get_request_data(self, row):
        col = self.data.get_request_data()
        request_data = self.excel.get_cell_value(row, col)
        if request_data == '':
            return None
        else:
            return request_data

    # 根据关键字拿到data
    def get_data_for_json(self, row):
        return self.json.get_data(self.get_request_data(row))

    # 获取预期结果
    def get_expect_data(self, row):
        col = self.data.get_expect()
        expect = self.excel.get_cell_value(row, col)
        if expect == '':
            return None
        else:
            return expect


# if __name__ == '__main__':
#     a = GetData()
#     lines = a.get_case_lines()
#     method = a.get_method(1)
#     url = a.get_url(1)
#     run = a.get_is_run(1)
#     headers = a.is_headers(1)
#     data = a.get_data_for_json(1)
#     expects = a.get_expect_data(1)
#     print(lines, url, run, method, headers, data, expects)
