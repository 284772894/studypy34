__author__ = 'Administrator'
#-*- coding: utf-8 -*-
from Base.Http import http_request
from Base.Threads import base_thread
from Base.OperateFile import base_file as baf
import Base.Matplotlib as bm
import Base.platform as bp
from Base.Check import base_check as bf
from Base.Sqlite import base_sqlite3
from Base.comm import http_commom
import Base.Excel as be
import Base.OperateXml as bo
import Base.OperateApp as bi
import Base.TestCase as bt
import Base.Crawler as bcr
import Base.Baselist as bl
import Base.BaseDict as bc
import Base.retest as ret
# import time
# import matplotlib.backends.backend_tkagg
# import tkinter
# import tkinter.filedialog
# import urllib3
import Base.getDir
hc = ""
br = ""
http_params = {"list_arg": [], "request_num": [], "response_time": [], "sum_03": 0, "sum_5": 0, "sum_1": 0, "sum_timeout": 0}
def sample_request(index=0):
    hc = http_commom()
    br = bo.read_xml()
    h = http_request(base_url=br['baseurl'], http_api=br['httpapi'], method=br['method'], http_params=br['postparams'])
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

                sum1 = float((http_params['sum_1']/int(br["count"]))*100)
                sum03 = float((http_params['sum_03']/int(br["count"]))*100)
                sum5 = float((http_params['sum_5']/int(br["count"]))*100)
                sum_timeout = float((http_params['sum_timeout']/int(br["count"]))*100)
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

def sample_list(index):
    calculation = {
        'create': lambda: base_sqlite3('c:/test.db').create_sql(),#创建sqlite3数据库
         'insert': lambda: base_sqlite3('c:/test.db').insert_sql(),#插入sqlite3数据
         'update': lambda: base_sqlite3('c:/test.db').update_sql(),#更新sqlite3数据
         'del': lambda: base_sqlite3('c:/test.db').del_sql(),#删除sql数据
         'select': lambda: base_sqlite3('c:/test.db').select_sql(),#查询sql数据
         'drop': lambda: base_sqlite3('c:/test.db').drop_table(),#删除sql中的表
         'read_file': lambda: baf('c:/test.txt', 'r').read_txt_rows(),#读取txt文件
         'request': lambda: sample_request(),#发送一个请求
         'read_excel': lambda: be.read_excel(),#读取excel数据
         'write_execl': lambda: be.write_excel(),#写excel
         'multi_thread': lambda: multi_thread(),#多线程请求
         'write_file': lambda: baf('c:/test.txt', 'a').write_txt(["eee", "rrr", "ttt"]),#写入数据到txt文件
         'sample_matp': lambda: sample_matp(),#柱形统计
         'sample_plot': lambda: sample_plot(),#曲线统计
         'sample_pie': lambda: sample_pie(),#饼形统计
         'platform': lambda:  bp.getAllProcessInfo(),#得到cpu,内存，网卡流量信息
         'dict_check': lambda: print(bf({'a': '123', 'b': '456'}, 'a').check_index()),#检查dict是否有a这个key
         'list_check': lambda: print(bf(['a', 'b', 'c'], '3').check_index()),#检查list是否包含3这个数据
         'check_file': lambda: baf('c:/test.txt').check_file(),#检查文件是否存在
         'mkdir_file': lambda: baf('c:/test.txt', 'w').mkdir_file(),#新建一个文件
         'revome_file': lambda: baf('c:/test.txt').remove_file(),#删除一个文件
         'read_xml': lambda: bo.read_xml(), #读取xml文件
         'install_app': lambda: bi.install("e/study/XX.apk"), #安装app
         'read_write_case': lambda: bt.read_write_case('D:/app/PICT/result.xls', 'D:/app/PICT/result1.xls'),#写测试案例
         'batch_install_app': lambda: bi.bact_install("E:\\study1\\Apps\\"),#批量安装app
         'Crawler': lambda : bcr.CrawlerFunc("http://tieba.baidu.com/p/3764230390")#多线程爬虫
         'getCurrentDir': lambda: Base.getDir.BaseGetCurrentDir(filename='conf.ini'), # 获取当前目录下的
         'BaseGetPreDir': lambda: Base.getDir.BaseGetPreDir(filename='conf.ini'), #获取上级目录的路径
         'BaseGetNextDir': lambda: Base.getDir.BaseGetNextDir(filename='conf.ini'),#下一个目录
         'attached_devices': lambda: bi.attached_devices(),# adb devices
         'badIterable': lambda: bl.badIterable(), # 不好的迭代读取
         'goodIterable': lambda: bl.goodIterable(),#好的迭代读取
         'listIterable': lambda: bl.listIterable(),#Enumerate list的运用
         'listIterable1': lambda: bl.listIterable1(),#Enumerate list的运用
         'sortList': lambda: bl.sortList([2, 4, 3, 5]),# list正序
         'reverseList': lambda: bl.reverseList([2, 4, 3, 5]),# list倒序
         'dictFactorial': lambda: bc.dictFactorial(),# 优雅打印dict的方式
         'testFindALl': lambda: ret.testFindALl(), #正则find的使用
         'testMatch': lambda: ret.testMatch(),#正则Match的使用
         'testSearch': lambda: ret.testSearch(),#正则searhch的使用
         'testSplit': lambda: ret.testSplit()# split的使用
    }
    return calculation[index]()


if __name__ == "__main__":
    sample_list('reverseList')
