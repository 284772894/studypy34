__author__ = 'Administrator'
# 正则测试
import re
def testFindALl():
    str_test = "out_2012.12.20.txt"
    re_reulst = re.findall(r"\d+", str_test)
    if re_reulst:
        print(re_reulst)
def testMatch():
    str_test = "out_2012.12.20.txt"
    re_reulst =re.match(r"\w+_(?P<year>\d+).(?P<month>\d+).(?P<day>\d+)", str_test)
    print(re_reulst.groupdict())

def testSearch():
    str_test = "out_2012.12.20.txt"
    re_reulst = re.search(r"\d+\.\d+\.\d+", str_test)
    print(re_reulst.group())

def testSplit():
    str_test = "out_2012.12.20.txt"
    re_reulst = re.split(r'\w+_(\d+)\.(\d+)\.(\d+)\.\w+', str_test)
    print(re_reulst)
testSplit()