__author__ = 'Administrator'
from pprint import pprint

# 优雅的打印dict
def dictFactorial():
    my_dict = {i: i * i for i in range(100)}
    pprint(my_dict)
