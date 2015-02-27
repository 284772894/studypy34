from xml.dom import minidom
from Base.OperateFile import base_file

def read_xml(file='c:/web.xml'):
    base_file(file).check_file()
    doc = minidom.parse(file)
    root = doc.documentElement
    nodes = root.getElementsByTagName("uu")
    for n in nodes:
        print('value=' + n.getAttribute("value"))
        print('key=' + n.childNodes[0].data)
