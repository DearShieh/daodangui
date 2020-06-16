import xlrd

data = xlrd.open_workbook('../data/API.xlsx')
tables = data.sheets()[0]
print(tables.nrows)
print(tables.cell_value(2, 3))

class OperationExcel:
    def __init__(self,file_name,sheet_id):
        self.data = self.get_data(file_name,sheet_id)

    def get_data(self,file_name,sheet_id):
        data = xlrd.open_workbook(file_name)
        tables = data.sheets()[sheet_id]        # 先拿sheet1、sheet2、sheet3等表
        return tables

if __name__ == '__main__':
    opers = OperationExcel()
    opers.get_data()