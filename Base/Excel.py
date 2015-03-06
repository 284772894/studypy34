__author__ = 'Administrator'
import xlrd
#https://pypi.python.org/pypi/xlrd/0.9.3
import xlsxwriter
#https://pypi.python.org/pypi/XlsxWriter/0.6.6#downloads
from Base.OperateFile import base_file
import os, sys


def read_excel(file='c:/test.xls'):
    #fileopen = open('D:/app/PICT/result.txt', 'w')
    dict_key = ['预约号', '客户姓名', '客户电话', '客户来源', '客户状态', '起始预约时间', '结束预约时间']
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
    #写入到文件中
    print(list)
    workbook = xlsxwriter.Workbook('D:/app/PICT/result1.xls')
    worksheet = workbook.add_worksheet()
    for i in range(len(list)):
        worksheet.write(i,0,list[i][dict_key[0]] + "," + list[i][dict_key[1]] + ',' + list[i][dict_key[2]] + ',' + list[i][dict_key[3]] +
        ',' + list[i][dict_key[4]] + ',' + list[i][dict_key[5]] + ',' + list[i][dict_key[6]])
    workbook.close()
    return list

def write_excel(file='c:/test.xlsx'):
    base_file(file).check_file()
    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()

    #worksheet.set_column('A:A', 20)
    worksheet.write('A1', 'Hello')
    bold = workbook.add_format({'bold': 1})
    worksheet.write('A2', 'World', bold)
    worksheet.write(2, 0, 123)
    #worksheet.insert_image('B5', 'logo.png')
    workbook.close()

