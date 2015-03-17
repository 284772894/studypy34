__author__ = 'Administrator'
#-*- coding: utf-8 -*-
from Base.Http import http_request
from Base.Threads import base_thread
from xml.dom import minidom
import os, sys
import numpy as np
import matplotlib.pyplot as pl
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg
import tkinter.filedialog
http_params = {"list_arg": [], "request_num": [], "response_time": [], "sum_03": 0, "sum_5": 0, "sum_1": 0}

def read_xml(file='c:/web.xml'):
    if not os.path.isfile(file):
        print('文件不存在' + file)
        sys.exit()

    doc = minidom.parse(file)
    root = doc.documentElement

    postparams = root.getElementsByTagName("postparams")
    ytitle = root.getElementsByTagName("ytitle")
    xtitle = root.getElementsByTagName("xtitle")
    title = root.getElementsByTagName("title")
    count = root.getElementsByTagName("count")
    baseurl = root.getElementsByTagName("baseurl")
    httpapi = root.getElementsByTagName("httpapi")
    method = root.getElementsByTagName("method")
    mat = root.getElementsByTagName("mat")
    xlim = root.getElementsByTagName("xlim")
    ylim = root.getElementsByTagName("ylim")

    list_xml = {}

    list_xml["ytitle"] = ytitle[0].getAttribute("value")
    list_xml["xtitle"] = xtitle[0].getAttribute("value")
    list_xml["title"] = title[0].getAttribute("value")
    list_xml["count"] = count[0].getAttribute("value")
    list_xml["baseurl"] = baseurl[0].getAttribute("value")
    list_xml["httpapi"] = httpapi[0].getAttribute("value")
    list_xml["method"] = method[0].getAttribute("value")
    list_xml["mat"] = mat[0].getAttribute("value")
    list_xml["xlim"] = xlim[0].getAttribute("value")
    list_xml["ylim"] = ylim[0].getAttribute("value")
    list_xml["postparams"] = postparams[0].getAttribute("value")
    return list_xml

br = read_xml()


def sample_request(index=0):
    h = http_request(base_url=br['baseurl'], http_api=br['httpapi'], method=br['method'])
    res = h.request(params=eval(br['postparams']))
    if res:
        res = '%.2f'%res
        #print(res)
        http_params['request_num'].append(index+1)
        http_params['response_time'].append(res)
        if index == int(br['count']) - 1: #如果循环总数循环结束，进行统计操作
            http_params['list_arg'].append(http_params['request_num'])
            http_params['list_arg'].append(http_params['response_time'])
            #print(hc.list_arg)
            if br['mat'] == "plot":
                mat_plot(http_params['list_arg'], title=br["title"], xtitle=br["xtitle"], ytitle=br["ytitle"], xlim=br["xlim"], ylim=br["ylim"])
            elif br['mat'] == "bar":
                mat_bar(http_params['list_arg'], title=br["title"], xtitle=br["xtitle"], ytitle=br["ytitle"])
            elif br['mat'] == 'pie':
                for j in http_params['list_arg'][1]:
                    temp = float(j)
                    if temp < 0.30:
                        http_params['sum_03'] += 1
                    if temp >= 0.30 and float(j) < 1.00:
                        http_params['sum_1'] += 1
                    if temp >= 1.00 and float(j) < 5.00:
                        http_params['sum_5'] += 1

                sum1 = int((http_params['sum_1']/int(br["count"]))*100)
                sum03 = int((http_params['sum_03']/int(br["count"]))*100)
                sum5 = int((http_params['sum_5']/int(br["count"]))*100)
                list_arg = None
                if (int(br["count"])) == (http_params['sum_1'] + http_params['sum_03'] + http_params['sum_5']):
                    list_arg = [[u'小于300ms请求共:' + str(http_params['sum_03'])+'个', u'300-1000ms请求共:' + str(http_params['sum_1'])+'个',
                                 u'1s-5s 请求共:'+str(http_params['sum_5'])+'个'], ['yellowgreen', 'gold', 'lightskyblue'], [sum03, sum1,sum5]]
                else:
                    sumother =int(br["count"]) - (http_params['sum_1'] + http_params['sum_03'] + http_params['sum_5'])
                    sum_o = int((sumother/br["count"])*100)
                    list_arg = [[u'小于300ms请求共:' + str(http_params['sum_03']) + '个', u'300-1000ms请求共:' + str(http_params['sum_1']) + '个',
                                 '1s-5s 请求共:'+str(http_params['sum_5']) + '个', u'大于5s请求共:'+str(sumother) + '个'], ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'], [sum03, sum1, sum5, sum_o]]
                print(list_arg)
                mat_pie(list_arg)
def multi_thread():
    threads = []
    for i in range(0, int(br["count"])):
        threads.append(base_thread(sample_request(i)))
    for j in range(0, int(br["count"])):
        threads[j].start()
    for k in range(0, int(br["count"])):
        threads[k].join()

def autolabel(ax, rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')

#柱形
def  mat_bar(args_list, title='登陆', xtitle='请求数量', ytitle='响应时间'):
    N = len(args_list[0])
    print(N)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, args_list[0], width, color='r')
    #womenMeans = args_list[1]
    #rects2 = ax.bar(ind+width, womenMeans, width, color='y')

    # add some
    ax.set_ylabel(ytitle)
    ax.set_xlabel(xtitle)
    ax.set_title(title)
    ax.set_xticks(ind+width)
    ax.set_xticklabels(args_list[1])

    #ax.legend((rects1[0], rects2[0]), ('Men', 'Women') )
    autolabel(ax, rects1)
    #autolabel(ax, rects2)
    plt.show()

#曲线[1, 2, 3, 4, 5]  [1, 4, 9, 16, 25]
def mat_plot(args_list, title='登陆', xtitle='请求数量', ytitle='响应时间', xlim=20, ylim=3):
    x1 = args_list[0]# Make x, y arrays for each graph
    y1 = args_list[1]
    #x2 = [1, 2, 4, 6, 8]
    #y2 = [2, 4, 8, 12, 16]
    pl.plot(x1, y1, 'r')# use pylab to plot x and y
    #pl.plot(x2, y2, 'g')
    pl.title(title)# give plot a title
    pl.xlabel(xtitle)# make axis labels
    pl.ylabel(ytitle)
    pl.xlim(0.0, int(xlim))
    pl.ylim(0.0, int(ylim))
    pl.show()
#默认曲线
def comm():
    n = 256
    X = np.linspace(-np.pi,np.pi,n,endpoint=True)
    Y = np.sin(2*X)
    pl.plot (X, Y+1, color='blue', alpha=1.00)
    pl.plot (X, Y-1, color='blue', alpha=1.00)
    pl.show()

 #饼状
def mat_pie(args_list, title="登陆"):
    #list_arg = [['Frogs', 'Hogs', 'Dogs', 'Logs'], ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'], [15, 30, 45, 10]]
    plt.figure(1, figsize=(6,6))
    pie_sum = []
    pie_title = []
    pie_color = []
    for i in range(len(args_list[2])): #[0 30, 0, 10] 对lsit中包含0的筛选出去
        if args_list[2][i] != 0:
            pie_sum.append(args_list[2][i])
            pie_title.append(args_list[0][i])
            pie_color.append(args_list[1][i])

    labels = pie_title
    sizes = pie_sum
    colors = pie_color
    plt.title(title, loc=u'left')
    #explode = (0, 0, 0, 0.1) # 对应sizes，数值越大就会凸出饼形
    pl.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    pl.axis('equal')
    pl.show()

multi_thread()
