from xml.dom import minidom
from Base.OperateFile import base_file
# web.xml 格式如下
# <?xml version="1.0" encoding="UTF-8" ?>
# <root>
# 	<uu value="cc">ccc-key</uu>
# 	<uu value="dd">dd-key</uu>
# </root>
def read_xml(file='c:/web.xml'):
    base_file(file).check_file()
    doc = minidom.parse(file)
    root = doc.documentElement
    nodes = root.getElementsByTagName("uu")
    for n in nodes:
        print('value=' + n.getAttribute("value"))
        print('key=' + n.childNodes[0].data)
