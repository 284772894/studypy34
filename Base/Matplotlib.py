__author__ = 'Administrator'
import numpy as np
import matplotlib.pyplot as pl
import matplotlib.pyplot as plt
from Base.comm import http_commom
def autolabel(ax, rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')

#柱形
def  mat_bar(args_list, args_dct):
    N = len(args_list[0])
    print(N)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, args_list[0], width, color='r')
    #womenMeans = args_list[1]
    #rects2 = ax.bar(ind+width, womenMeans, width, color='y')

    # add some
    ax.set_ylabel(args_dct[u'ytitle'])
    ax.set_xlabel(args_dct[u'xtitle'])
    ax.set_title(args_dct[u'title'])
    ax.set_xticks(ind+width)
    ax.set_xticklabels(args_list[1])

    #ax.legend((rects1[0], rects2[0]), ('Men', 'Women') )
    autolabel(ax, rects1)
    #autolabel(ax, rects2)
    plt.show()

#曲线[1, 2, 3, 4, 5]  [1, 4, 9, 16, 25]
def mat_plot(args_list, args_dict):
    x1 = args_list[0]# Make x, y arrays for each graph
    y1 = args_list[1]
    #x2 = [1, 2, 4, 6, 8]
    #y2 = [2, 4, 8, 12, 16]
    pl.plot(x1, y1, 'r')# use pylab to plot x and y
    #pl.plot(x2, y2, 'g')
    pl.title(args_dict[u'title'])# give plot a title
    pl.xlabel(args_dict[u'xtitle'])# make axis labels
    pl.ylabel(args_dict[u'ytitle'])
    pl.xlim(0.0, http_commom().xlim)# 设置横轴的上下限
    pl.ylim(0.0, http_commom().ylim)
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
def mat_pie(args_list):
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
    plt.title(http_commom().dct_arg[u"title"], loc=u'left')
    #explode = (0, 0, 0, 0.1) # 对应sizes，数值越大就会凸出饼形
    pl.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    pl.axis('equal')
    pl.show()

