# study
python 版本为3.4

调用方式为：
 sample_list(param)
 #param参数对应sample_list的key就可以了
 
 如：sample_list('request')

        'create': lambda: bs.create_sql(), #创建sqlite3数据库
        
        'insert': lambda: bs.insert_sql(),#插入sqlite3数据
        
        'update': lambda: bs.update_sql(),#更新sqlite3数据
        
        'del': lambda: bs.del_sql(),#删除sql数据
        
        'select': lambda: bs.select_sql(),#查询sql数据
        
        'drop': lambda: bs.drop_table(),#删除sql中的表
        
        'read_file': lambda: base_file('c:/test.txt', 'r').read_txt_rows(),#读取txt文件
        'request': lambda: sample_request(),#发送一个请求
        
        'read_excel': lambda: base_excel().read_excel(),#读取excel数据
        
        'write_execl': lambda: base_excel.write_excel(),#写excel
        'multi_thread': lambda: multi_thread(),#多线程请求
        
        'write_file': lambda: base_file('c:/test.txt', 'a').write_txt(["eee", "rrr", "ttt"]),#写入数据到txt文件
        'sample_matp': lambda: sample_matp(),#柱形统计
        
        'sample_plot': lambda: sample_plot(),#曲线统计
        
        'sample_pie': lambda: sample_pie(),#饼形统计
        
        'platform': lambda:  bp.getAllProcessInfo(),#得到cpu,内存，网卡流量信息
        
        'dict_check': lambda: print(base_check({'a': '123', 'b': '456'}, 'a').check_index()),#检查dict是否有a这个key
        
        'list_check': lambda: print(base_check(['a', 'b', 'c'], '3').check_index()),#检查list是否包含3这个数据
        'check_file': lambda: bf.check_file(),#检查文件是否存在
        
        'mkdir_file': lambda: base_file('c:/test.txt', 'w').mkdir_file(),#新建一个文件
        
        'revome_file': lambda: bf.remove_file(),#删除一个文件
	'read_xml': lambda: bo.read_xml() #读取xml文件    

