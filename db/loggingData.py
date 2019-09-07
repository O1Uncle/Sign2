import xlrd  # 读取模块
from awesome.plugins.dir import init

path = 'F:\VSCoding\Code\python\Pyproject\\test01\jk1703.xls'
# 获取整个Excel表格
workBook = xlrd.open_workbook(path)
# 获取所有的sheet
sheetList = workBook.sheets()
# 获取某一个sheet
# sheet1 = sheetList[0] #获取第一个sheet
# 表中最大的行，最大的列
sheet1 = workBook.sheet_by_name(u'jk1703')
nrows = sheet1.nrows
ncols = sheet1.ncols
# print('nrows = ', nrows)
'''
通过列表的下标，直接获取第一个sheet
workBook.sheet_by_index(0)
通过sheet名来获取sheet
workBook.sheet_by_name(u'Sheet1')
'''
# #获取第一行的数据
# for i in range(0, nrows):
#     for j in range(0, ncols):
#         if(sheet1.cell(i, j) == ' '):
#             sheet1.cell(i, j) = 0
# print(sheet1.row_values(1))
# 打印整个表格
init()
for i in range(2, nrows):
    colList = sheet1.row_values(i)
    # cn.addStu(int(colList[]))
    cn.addStu(int(colList[0]), int(colList[2]), str(colList[1]),  0)
    # print(colList)
