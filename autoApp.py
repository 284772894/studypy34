__author__ = 'Administrator'
from uiautomator import Device
import unittest
import time
from Base.OperateApp import base_adb_app


class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        self.d = Device('192.168.1.62:5555')
        self.d.screen.on()
        base_adb_app().open_app('io.appium.unlock', 'io.appium.unlock.Unlock') #打开自动解锁app
    def tearDown(self):
        print("down")

    def test_case1(self):
        print("testcase1")
        #self.d(className="android.widget.ListView").child(text="邓胜强").click()
        base_adb_app().open_app('com.tencent.mm', 'com.tencent.mm.ui.LauncherUI')
        self.d(text='通讯录').click()
        #self.d.swipe(40, 2000, 40, 40, 10)
        # self.d.swipe(60, 1700, 40, 40, 10)
        # time.sleep(1)
        # self.d.swipe(60, 1700, 60, 400, 10)



        t = self.d(className="android.widget.ListView") .child_by_text("阿布",allow_scroll_search=True,className="android.view.View")
        t.click()

        self.d(text='发消息').click()
        self.d(className="android.widget.TextView")[0].click
        #36,1278,200,300t
        #[270,1772][540,1905]u
if __name__ == '__main__':
    unittest.main()
    # if device(text='Force Close').exists:
    #io.appium.unlock  io.appium.unlock.Unlock
    #com.tencent.mm com.tencent.mm.ui.LauncherUI
    #d.press.back()
    #d(text="Settings").set_text("My text...")  # set the text