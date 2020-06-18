import xlrd


# dataconfig = xlrd.open_workbook('../dataconfig/API.xlsx')
# tables = dataconfig.sheets()[0]
# print(tables.nrows)
# print(tables.cell_value(2, 3))


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/API.xlsx'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheet内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]  # 先拿sheet1、sheet2、sheet3等表
        return tables

    # 获取单元行行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某个单元格的内容
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

# if __name__ == '__main__':
#     opers = OperationExcel()
#     print(opers.get_data().nrows)
#     print(opers.get_lines())
#     print(opers.get_cell_value(1, 5))
