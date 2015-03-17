__author__ = 'Administrator'
import xlrd
#https://pypi.python.org/pypi/xlrd/0.9.3
import xlsxwriter
#https://pypi.python.org/pypi/XlsxWriter/0.6.6#downloads
from Base.OperateFile import base_file
import os, sys


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

