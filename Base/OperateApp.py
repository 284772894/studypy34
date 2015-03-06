# -*- coding: utf-8 -*-

import os
import time
import sys

#需要在脚本所在目录AndroidAdb目录下有个AndroidAdb.exe程序，该adb可以支持安装以中文命名的apk
#需要将apk文件放在脚本所在目录下的Apps目录下

class base_adb_app:
    def __init__(self):
        print("")
    #检查AndroidAdb.exe
    def check_adb(self):
        if os.path.isfile("%s\\AndroidAdb\\AndroidAdb.exe" % os.getcwd()):
            return True
        else:
            return False

    #检查Apps目录
    def check_dir(self):
        if os.path.isdir("%s\\Apps" % os.getcwd()):
            return True
        else:
            return False

    def install(self):
        count = 0
        apps_dir = "%s\\Apps" % os.getcwd()
        for path, subdir, files in os.walk(apps_dir):
            for apk in files:
                os.popen("%s\\AndroidAdb\\AndroidAdb.exe install %s" % (os.getcwd(), os.path.join(path, apk)))
                count += 1

        print("\n%s apps install complete." % str(count))

     #install app
    def start_install(self):
        if base_adb_app().check_adb():
            pass
        else:
            print("AndroidAdb.exe not exist.")
            time.sleep(3)
            sys.exit(0)

        if base_adb_app().check_dir():
            pass
        else:
            print("Apps Directory not exist")
            time.sleep(3)
            sys.exit(0)
        base_adb_app().install()

    #unstall app
    def uninstall(self,packageName):
        os.popen("adb wait-for-device")
        print("start uninstall...")
        os.popen("adb uninstall %s" % packageName)

    def open_app(self, packagename, activity):
       os.popen("adb wait-for-device")
       print("start open app")
       os.popen("adb shell am start -n %s/%s" % (packagename, activity))