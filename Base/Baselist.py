l = [2, 4, 3, 5]
str = "bcdea"
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

#[(0, 'a'), (1, 'b'), (2, 'c')]
def listIterable():
    le = list(enumerate('abc'))
    return le
#[(1, 'a'), (2, 'b'), (3, 'c')]
def listIterable1():
    le = list(enumerate('abc', 1))
# 正序
def sortList(li):
    li.sort()
    return li
# 倒序
def reverseList(li):
    # li.reverse()
    temp = li[::-1]
    print(temp)
    return temp
