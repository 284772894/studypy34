__author__ = 'Administrator'
import os
# 获取当前目录下的
def BaseGetCurrentDir(filename=''):
   return str(os.getcwd()) + '/' + filename
#获取上级目录的路径
def BaseGetPreDir(filename=''):
    path = os.getcwd()
    parent_path = os.path.dirname(path)
    return str(parent_path) + '/' + filename
# print(BaseGetCurrentDir(filename='conf.ini'))
# 下一个目录,parent_path)[3] 这里等于Base
def BaseGetNextDir(filename=''):
    path = os.getcwd()
    parent_path = os.path.dirname(path)
    return parent_path + '/' +os.listdir(parent_path)[3] + "/" + filename
