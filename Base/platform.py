__author__ = 'Administrator'
import platform
import psutil
#https://pypi.python.org/pypi?:action=display&name=psutil#downloads
import time

def base_platform():
    print(platform.architecture()) # 32 or 64
    print(platform.system()) #os
    print(platform.version()) #os version
    print(platform.machine()) #cpu info
    print(platform.node()) #computer name
    print(platform.uname()) #system info
    print(platform.python_version()) #python version

def getAllProcessInfo():
    #查看cpu的信息
    print (u"CPU 个数 %s"%psutil.cpu_count())
    print (u"物理CPU个数 %s"%psutil.cpu_count(logical=False))
    #查看内存信息
    print(u"系统内存 "+str(psutil.virtual_memory()))
    #网卡，可以得到网卡属性，连接数，当前流量等信息
    print(psutil.net_io_counters())
    bytes_sent = '{0:.2f} kb'.format(psutil.net_io_counters().bytes_recv / 1024)
    bytes_rcvd = '{0:.2f} kb'.format(psutil.net_io_counters().bytes_sent / 1024)
    print (u"网卡接收流量 %s 网卡发送流量 %s"%(bytes_rcvd, bytes_sent))