# import xlrd  # 读取模块
# from dir import init
# from dir import get

# path = 'F:\VSCoding\Code\python\Pyproject\\test01\jk1703.xls'
# # 获取整个Excel表格
# workBook = xlrd.open_workbook(path)

# sheet1 = workBook.sheet_by_name(u'jk1703')
# nrows = sheet1.nrows
# init()

# for i in range(2, nrows):
#     colList = sheet1.row_values(i)
#     get().addStu('计科1703', str(colList[1]), int(colList[2]), int(colList[0]), 0)
