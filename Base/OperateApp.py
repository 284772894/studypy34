# -*- coding: utf-8 -*-

import os
import time
import sys
import glob
from Base.Threads import base_thread

#单文件安装
def install(filename):
    print(filename)
    os.popen("adb install %s" % filename)

#批量安装app,多线程安装
def bact_install(dir):
    if os.path.isdir(dir):
        starttime = time.time()
        filelist= glob.glob(dir + "*.apk")
        threads = []
        for i in range(0, len(filelist)):
            threads.append(base_thread(install(filelist[i])))
        for j in range(0, len(filelist)):
            threads[j].start()
        for k in range(0, len(filelist)):
            threads[k].join()
        print("总运行时间"+str(time.time() - starttime))
    else:
        print("目录不存在")
        sys.exit(0)

#unstall app
def uninstall(packageName):
    os.popen("adb wait-for-device")
    print("start uninstall...")
    os.popen("adb uninstall %s" % packageName)

def open_app(packagename, activity):
   os.popen("adb wait-for-device")
   print("start open app")
   os.popen("adb shell am start -n %s/%s" % (packagename, activity))