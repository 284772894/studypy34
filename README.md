# python3 日常学习积累
* 调用方式为：sample_list(param)
* param参数对应sample_list的key就可以了
* 如：sample_list('request')
## 功能说明
* 'create': lambda: base_sqlite3('c:/test.db').create_sql(),#创建sqlite3数据库
* 'insert': lambda: base_sqlite3('c:/test.db').insert_sql(),#插入sqlite3数据
* 'update': lambda: base_sqlite3('c:/test.db').update_sql(),#更新sqlite3数据
* 'del': lambda: base_sqlite3('c:/test.db').del_sql(),#删除sql数据
* 'select': lambda: base_sqlite3('c:/test.db').select_sql(),#查询sql数据
* 'drop': lambda: base_sqlite3('c:/test.db').drop_table(),#删除sql中的表
* 'read_file': lambda: baf('c:/test.txt', 'r').read_txt_rows(),#读取txt文件
* 'request': lambda: sample_request(),#发送一个请求
* 'read_excel': lambda: be.read_excel(),#读取excel数据
* 'write_execl': lambda: be.write_excel(),#写excel
* 'multi_thread': lambda: multi_thread(),#多线程请求
* 'write_file': lambda: baf('c:/test.txt', 'a').write_txt(["eee", "rrr", "ttt"]),#写入数据到txt文件
* 'sample_matp': lambda: sample_matp(),#柱形统计
* 'sample_plot': lambda: sample_plot(),#曲线统计
* 'sample_pie': lambda: sample_pie(),#饼形统计
* 'platform': lambda:  bp.getAllProcessInfo(),#得到cpu,内存，网卡流量信息
* 'dict_check': lambda: print(bf({'a': '123', 'b': '456'}, 'a').check_index()),#检查dict是否有a这个key
* 'list_check': lambda: print(bf(['a', 'b', 'c'], '3').check_index()),#检查list是否包含3这个数据
* 'check_file': lambda: baf('c:/test.txt').check_file(),#检查文件是否存在
* 'mkdir_file': lambda: baf('c:/test.txt', 'w').mkdir_file(),#新建一个文件
* 'revome_file': lambda: baf('c:/test.txt').remove_file(),#删除一个文件
* 'read_xml': lambda: bo.read_xml(), #读取xml文件
* 'install_app': lambda: bi.install("e/study/XX.apk"), #安装app
* 'read_write_case': lambda: bt.read_write_case('D:/app/PICT/result.xls', 'D:/app/PICT/result1.xls'),#写测试案例
* 'batch_install_app': lambda: bi.bact_install("E:\\study1\\Apps\\"),#批量安装app
* 'Crawler': lambda : bcr.CrawlerFunc("http://tieba.baidu.com/p/3764230390")#多线程爬虫
* 'getCurrentDir': lambda: Base.getDir.BaseGetCurrentDir(filename='conf.ini'), # 获取当前目录下的
* 'BaseGetPreDir': lambda: Base.getDir.BaseGetPreDir(filename='conf.ini'), #获取上级目录的路径
* 'BaseGetNextDir': lambda: Base.getDir.BaseGetNextDir(filename='conf.ini'),#下一个目录
* 'attached_devices': lambda: bi.attached_devices(),# adb devices
* 'badIterable': lambda: bl.badIterable(), # 不好的迭代读取
* 'goodIterable': lambda: bl.goodIterable(),#好的迭代读取
* 'listIterable': lambda: bl.listIterable(),#Enumerate list的运用
* 'listIterable1': lambda: bl.listIterable1(),#Enumerate list的运用
* 'sortList': lambda: bl.sortList([2, 4, 3, 5]),# list正序
* 'reverseList': lambda: bl.reverseList([2, 4, 3, 5]),# list倒序
* 'dictFactorial': lambda: bc.dictFactorial(),# 优雅打印dict的方式
* 'testFindALl': lambda: ret.testFindALl(), #正则find的使用
* 'testMatch': lambda: ret.testMatch(),#正则Match的使用
* 'testSearch': lambda: ret.testSearch(),#正则searhch的使用
* 'testSplit': lambda: ret.testSplit()# split的使用

