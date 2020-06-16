import xlrd

data = xlrd.open_workbook('../data/API.xlsx')
tables = data.sheets()[0]
print(tables.nrows)
print(tables.cell_value(2, 3))
