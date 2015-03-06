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
#test
hc = http_commom()

def sample_request(index=0):
    h = http_request(hc.base_url, "", hc.http_api, hc.method)
    res = h.request('')
    print(res)
    if res:
        res = '%.2f'%res
        #print(res)
        hc.request_num.append(index+1)
        hc.response_time.append(res)
        if index == hc.count - 1: #如果循环总数循环结束，进行统计操作
            hc.list_arg.append(hc.request_num)
            hc.list_arg.append(hc.response_time)
            #print(hc.list_arg)
            if hc.mat == "plot":
                bm.mat_plot(hc.list_arg, hc.dct_arg)
            elif hc.mat == "bar":
                bm.mat_bar(hc.list_arg, hc.dct_arg)
            elif hc.mat == 'pie':
                for j in hc.list_arg[1]:
                    temp = float(j)
                    #print(temp)
                    if temp < 0.30:
                        hc.sum_03 += 1
                        #print(hc.sum_03)
                    if temp >= 0.30 and float(j) < 1.00:
                        hc.sum_1 += 1
                    if temp >= 1.00 and float(j) < 5.00:
                        hc.sum_5 += 1

                sum1 = int((hc.sum_1/hc.count)*100)
                sum03 = int((hc.sum_03/hc.count)*100)
                sum5 = int((hc.sum_5/hc.count)*100)
                list_arg = None
                if hc.count == (hc.sum_1 + hc.sum_03 + hc.sum_5):
                    list_arg = [[u'小于300ms请求共:' + str(hc.sum_03)+'个', u'300-1000ms请求共:' + str(hc.sum_1)+'个',
                                 u'1s-5s 请求共:'+str(hc.sum_5)+'个'], ['yellowgreen', 'gold', 'lightskyblue'], [sum03, sum1, sum5]]
                else:
                    sumother = hc.count - (hc.sum_1 + hc.sum_03 + hc.sum_5)
                    sum_o = int((sumother/hc.count)*100)
                    list_arg = [[u'小于300ms请求共:' + str(hc.sum_03) + '个', u'300-1000ms请求共:' + str(hc.sum_1) + '个',
                                 '1s-5s 请求共:'+str(hc.sum_5) + '个', u'大于5s请求共:'+str(sumother) + '个'], ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'], [sum03, sum1, sum5, sum_o]]
                print(list_arg)
                bm.mat_pie(list_arg)
def multi_thread():
    threads = []
    for i in range(0, hc.count):
        threads.append(base_thread(sample_request(i)))
    for j in range(0, hc.count):
        threads[j].start()
    for k in range(0, hc.count):
        threads[k].join()

def sample_matp():
    #柱形
    list_arg = [[20, 35, 30, 35, 27], ['t1', 't2', 't3', 't4', 't5']]
    dct_arg = {'ytitle': 'this is y title', 'xtitle': 'this is x title', 'title': 'this is title'}
    bm.mat_bar(list_arg, dct_arg)

def sample_plot():
    #曲线
    list_arg = [[1, 2, 3, 4, 5], [1, 4, 9, 16, 25]]
    dct_arg = {'ytitle': 'this is y title', 'xtitle': 'this is x title', 'title': 'this is title'}
    bm.mat_plot(list_arg, dct_arg)

def sample_pie():
    #饼形
    list_arg = [['Frogs', 'Hogs', 'Dogs', 'Logs'], ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'], [15, 30, 45, 10]]
    bm.mat_pie(list_arg)


def sample_list(index):
    calculation = {
        'create': lambda: base_sqlite3('c:/test.db').create_sql(),
        'insert': lambda: base_sqlite3('c:/test.db').insert_sql(),
        'update': lambda: base_sqlite3('c:/test.db').update_sql(),
        'del': lambda: base_sqlite3('c:/test.db').del_sql(),
        'select': lambda: base_sqlite3('c:/test.db').select_sql(),
        'drop': lambda: base_sqlite3('c:/test.db').drop_table(),
        'read_file': lambda: base_file('c:/test.txt', 'r').read_txt_rows(),
        'request': lambda: sample_request(),
        'read_excel': lambda: be.read_excel('D:/app/PICT/result.xls'),
        'write_excel': lambda: be.write_excel('c:/test.xls'),
        'multi_thread': lambda: multi_thread(),
        'write_file': lambda: base_file('c:/test.txt', 'a').write_txt(["eee", "rrr", "ttt"]),
        'sample_matp': lambda: sample_matp(),
        'sample_plot': lambda: sample_plot(),
        'sample_pie': lambda: sample_pie(),
        'platform': lambda:  bp.getAllProcessInfo(),
        'dict_check': lambda: base_check({'a': '123', 'b': '456'}, 'a').check_index(),
        'list_check': lambda: base_check(['a', 'b', 'c'], '3').check_index(),
        'check_file': lambda: base_file().check_file(),
        'mkdir_file': lambda: base_file('c:/test.txt', 'w').mkdir_file(),
        'revome_file': lambda: base_file('c:/test.xls').remove_file(),
        'read_xml': lambda: bo.read_xml(),
        'install_app': lambda: bi.base_adb_app().start_install()
    }
    return calculation[index]()

if __name__ == "__main__":
    sample_list('read_excel')
    #adb shell 'am start -n ｛包(package)名｝/｛包名｝.{活动(activity)名称}'
    #com.example.ffdianxun1_1
    #com.example.ffdianxun1_1.EntryPageActivity