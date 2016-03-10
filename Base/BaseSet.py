__author__ = 'Administrator'
def testSet():
    my_set = {i * 15 for i in range(100)}
    print(my_set)
# 交集
def intersection():
    x = set("span")
    y = set("pta")
    print(x&y)
# 合集
def collection():
    x = set("span")
    y = set("pta")
    print(x|y)
# 差集
def subtract():
    x = set("span")
    y = set("pta")
    print(x-y)

#去掉重复数据
def removeRepeat():
    a = [11,22,33,44,11,22]
    b = set(a)
    print(b)
    c = [i for i in b]
    print(c)
removeRepeat()