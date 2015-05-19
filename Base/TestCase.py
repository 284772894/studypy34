import xlrd
#https://pypi.python.org/pypi/xlrd/0.9.3
import xlsxwriter
#https://pypi.python.org/pypi/XlsxWriter/0.6.6#downloads
from Base.OperateFile import base_file
import os, sys

def read_write_case(read_excel='D:/app/PICT/result.xls', write_excel='D:/app/PICT/result1.xls'):
    #dict_key = ['起始价格', '结束价格', '钻重起始重量', '钻重结束重量', '颜色', '净度', '切工', '抛光', '对称', '荧光', '形状', '证书']
    dict_key = ['订单状态', '开始时间', '结束时间', '会员信息']
    base_file(read_excel).check_file()
    base_file(write_excel).check_file()
    data = xlrd.open_workbook(read_excel)
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
    #写入到文件中
    print(list)
    workbook = xlsxwriter.Workbook(write_excel)
    worksheet = workbook.add_worksheet()
    for i in range(len(list)):
        worksheet.write(i, 0, "设置条件：" + "\n" + list[i][dict_key[0]] + "," + list[i][dict_key[1]] + ',' + list[i][dict_key[2]] +',' + list[i][dict_key[3]] +"\n" + "点击提交")

    workbook.close()
    return list