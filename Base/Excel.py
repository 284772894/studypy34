__author__ = 'Administrator'
import  sys
sys.path.append("/Base")
import xlrd
#https://pypi.python.org/pypi/xlrd/0.9.3
import xlsxwriter
#https://pypi.python.org/pypi/XlsxWriter/0.6.6#downloads
from Base.OperateFile import base_file



def read_excel(file='c:/test.xls'):
    base_file(file).check_file()
    data = xlrd.open_workbook(file)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    ncols = table.ncols
    colnames = table.row_values(0) #one rows data
    list = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                row[i] = colnames[i] + row[i]
                app[colnames[i]] = row[i]
            list.append(app)
    return list

def write_excel(file='d:/result.xlsx', httpurl="", httpmethod="", response_time=[]):
    base_file(file).mkdir_file()
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()
    #worksheet.set_column('A:A', 20)
    worksheet.write(0, 0, "接口URL")
    worksheet.write(0, 1, "请求方法")
    worksheet.write(0, 2, "响应时间")
    for i in range(len(response_time)):
        worksheet.write(i + 1, 0, httpurl[i])
        worksheet.write(i + 1, 1, httpmethod)
        if response_time[i] == 0:
            worksheet.write(i + 1, 2, "请求超时")
        else:
             worksheet.write(i + 1, 2, response_time[i])
    #worksheet.insert_image('B5', 'logo.png')
    workbook.close()

