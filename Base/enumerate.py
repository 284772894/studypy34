__author__ = 'Administrator'
def badIterable():
    i = 0
    iterable = ["a", "b", "c"]
    for item in iterable:
        print(i, item)
        i += 1
def goodIterable():
    iterable = ["a", "b", "c"]
    for i, item in enumerate(iterable):
        print(i, item)
def listIterable():
    le = list(enumerate('abc'))
    print(le)
def listIterable1():
    le = list(enumerate('abc', 1))
    print(le)
def forDict():
    my_dict = {i: i * i for i in range(100)}
    my_set = {i * 15 for i in range(100)}
    print(type(my_dict))
    print(type(my_set))

forDict()