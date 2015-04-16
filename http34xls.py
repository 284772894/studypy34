__author__ = 'Administrator'
#-*- coding: utf-8 -*-
import sys,os
sys.path.append("/Base")
from Base.Http import http_request
from Base.Threads import base_thread
import Base.OperateXml as bo
from Base.comm import http_commom as hc
import tkinter
import tkinter.filedialog
import urllib.request
import urllib.parse
import http.client
import time
import socket
import xlrd
import xlsxwriter
import traceback
br = bo.read_xml()

http_params = {"list_arg": [], "request_num": [], "response_time": [], "sum_03": 0, "sum_5": 0, "sum_1": 0, "sum_timeout": 0}
temp = 0
def sample_request():

    for l in range(len(br['httpapi'])):
        h = http_request(base_url=br['baseurl'], http_api=br['httpapi'][l], method=br['method'])
        res = h.request()
        if res:
            res = '%.2f'%res
            #print(res)
            http_params['response_time'].append(res)
        else:
            http_params['response_time'].append("0")

def multi_thread():
    threads = []
    for i in range(0, int(br["count"])):
        threads.append(base_thread(sample_request()))
    for j in range(0, int(br["count"])):
        threads[j].start()
    for k in range(0, int(br["count"])):
        threads[k].join()
def write_result():

  write_excel(httpurl=hc.list_arg, httpmethod=br['method'], response_time=hc.response_time)



def write_excel(file='d:/result.xlsx', httpurl="", httpmethod="", response_time=[]):
    if not os.path.isfile(file):
            f = open(file, "w")
            f.close()
            print(u"创建文件成功")


    workbook = xlsxwriter.Workbook(file)
    worksheet = workbook.add_worksheet()
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
    workbook.close()

multi_thread()
write_result()