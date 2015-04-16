__author__ = 'Administrator'
#-*- coding: utf-8 -*-
from Base.Http import http_request
from Base.Threads import base_thread
from Base.OperateFile import base_file
import Base.Matplotlib as bm
import Base.platform as bp
from Base.Check import base_check
from Base.Sqlite import base_sqlite3
from Base.comm import http_commom
import Base.Excel as be
import Base.OperateXml as bo
import Base.OperateApp as bi
import Base.TestCase as bt
import time
import autoApp as au
import matplotlib.backends.backend_tkagg
import tkinter
import tkinter.filedialog
import urllib3
hc = http_commom()
br = bo.read_xml()
http_params = {"list_arg": [], "request_num": [], "response_time": [], "sum_03": 0, "sum_5": 0, "sum_1": 0, "sum_timeout": 0}

def sample_request(index=0):
    h = http_request(base_url=br['baseurl'], http_api=br['httpapi'], method=br['method'])
    res = h.request()
    http_params['request_num'].append(index+1)
    if res:
        res = '%.2f'%res
        #print(res)
        http_params['response_time'].append(res)

    else:
        http_params['response_time'].append("0")
    if index == int(br['count']) - 1: #如果循环总数循环结束，进行统计操作
            http_params['list_arg'].append(http_params['request_num'])
            http_params['list_arg'].append(http_params['response_time'])
            #print(hc.list_arg)
            if br['mat'] == "plot":
                bm.mat_plot(http_params['list_arg'], title=br["title"], xtitle=br["xtitle"], ytitle=br["ytitle"], xlim=br["xlim"], ylim=br["ylim"])
            elif br['mat'] == "bar":
                bm.mat_bar(http_params['list_arg'], title=br["title"], xtitle=br["xtitle"], ytitle=br["ytitle"])
            elif br['mat'] == 'pie':
                for j in http_params['list_arg'][1]:
                    temp = float(j)
                    if temp < 0.30 and temp != 0.0:
                        http_params['sum_03'] += 1
                    if temp >= 0.30 and float(j) < 1.00:
                        http_params['sum_1'] += 1
                    if temp >= 1.00 and float(j) < 5.00:
                        http_params['sum_5'] += 1
                    if temp == 0:
                         http_params['sum_timeout'] += 1

                sum1 = int((http_params['sum_1']/int(br["count"]))*100)
                sum03 = int((http_params['sum_03']/int(br["count"]))*100)
                sum5 = int((http_params['sum_5']/int(br["count"]))*100)
                sum_timeout = int((http_params['sum_timeout']/int(br["count"]))*100)
                list_arg = None
                if (int(br["count"])) == (http_params['sum_1'] + http_params['sum_03'] + http_params['sum_5'] + http_params['sum_timeout']):
                    list_arg = [[u'小于300ms请求共:' + str(http_params['sum_03'])+'个', u'300-1000ms请求共:' + str(http_params['sum_1'])+'个',
                                 u'1s-5s 请求共:'+str(http_params['sum_5'])+'个', u'请求超时共:'+str(http_params['sum_timeout'])+'个'], ['yellowgreen', 'gold', 'lightskyblue', 'red'], [sum03, sum1,sum5, sum_timeout]]
                else:
                    sumother =int(br["count"]) - (http_params['sum_1'] + http_params['sum_03'] + http_params['sum_5'] + http_params['sum_timeout'])
                    sum_o = 0
                    if sumother!= 0:
                        sum_o = (sumother/int(br["count"]))*100
                    list_arg = [[u'小于300ms请求共:' + str(http_params['sum_03']) + '个', u'300-1000ms请求共:' + str(http_params['sum_1']) + '个',
                                 '1s-5s 请求共:'+str(http_params['sum_5']) + '个', u'大于5s请求共:'+str(sumother) + '个', u'请求超时共:'+str(http_params['sum_timeout'])+'个'], ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red'], [sum03, sum1, sum5, sum_o, sum_timeout]]
                print(list_arg)
                bm.mat_pie(list_arg, title=br["title"])
def multi_thread():
    starttime = time.time()
    threads = []
    for i in range(0, int(br["count"])):
        threads.append(base_thread(sample_request(index=i)))
    for j in range(0, int(br["count"])):
        threads[j].start()
    for k in range(0, int(br["count"])):
        threads[k].join()

def sample_matp():
    #柱形
    list_arg = [[20, 35, 30, 35, 27], ['t1', 't2', 't3', 't4', 't5']]
    bm.mat_bar(list_arg)

def sample_plot():
    #曲线
    list_arg = [[1, 2, 3, 4, 5], [1, 4, 9, 16, 25]]
    bm.mat_plot(list_arg)

def sample_pie():
    #饼形
    list_arg = [['Frogs', 'Hogs', 'Dogs', 'Logs'], ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'], [15, 30, 45, 10]]
    bm.mat_pie(list_arg)

multi_thread()
# def sample_list(index):
#     calculation = {
#         'create': lambda: base_sqlite3('c:/test.db').create_sql(),
#         'insert': lambda: base_sqlite3('c:/test.db').insert_sql(),
#         'update': lambda: base_sqlite3('c:/test.db').update_sql(),
#         'del': lambda: base_sqlite3('c:/test.db').del_sql(),
#         'select': lambda: base_sqlite3('c:/test.db').select_sql(),
#         'drop': lambda: base_sqlite3('c:/test.db').drop_table(),
#         'read_file': lambda: base_file('c:/test.txt', 'r').read_txt_rows(),
#         'request': lambda: sample_request(),
#         'read_excel': lambda: be.read_excel('D:/app/PICT/result.xls'),
#         'write_excel': lambda: be.write_excel('c:/test.xls'),
#         'multi_thread': lambda: multi_thread(),
#         'write_file': lambda: base_file('c:/test.txt', 'a').write_txt(["eee", "rrr", "ttt"]),
#         'sample_matp': lambda: sample_matp(),
#         'sample_plot': lambda: sample_plot(),
#         'sample_pie': lambda: sample_pie(),
#         'platform': lambda:  bp.getAllProcessInfo(),
#         'dict_check': lambda: base_check({'a': '123', 'b': '456'}, 'a').check_index(),
#         'list_check': lambda: base_check(['a', 'b', 'c'], '3').check_index(),
#         'check_file': lambda: base_file().check_file(),
#         'mkdir_file': lambda: base_file('c:/test.txt', 'w').mkdir_file(),
#         'revome_file': lambda: base_file('c:/test.xls').remove_file(),
#         'read_xml': lambda: bo.read_xml(),
#         'install_app': lambda: bi.install("e/study/XX.apk"),
#         'read_write_case': lambda: bt.read_write_case('D:/app/PICT/result.xls', 'D:/app/PICT/result1.xls'),
#         'batch_install_app': lambda: bi.bact_install("E:\\study1\\Apps\\")
#     }
#     return calculation[index]()
#
#
# if __name__ == "__main__":
#     sample_list('multi_thread')
    #adb shell 'am start -n ｛包(package)名｝/｛包名｝.{活动(activity)名称}'
    #com.example.ffdianxun1_1
    #com.example.ffdianxun1_1.EntryPageActivity