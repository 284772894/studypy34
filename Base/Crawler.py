import urllib.request as request
from bs4 import BeautifulSoup
from Base.Threads import base_thread
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
#https://pypi.python.org/pypi/BeautifulSoup/3.2.1
path = 'e:/apps/pic/'
def CrawlerFunc(url):
    list_img = getUrl(url)
    multi_thread(len(list_img), downloadImg(list_img))
def getUrl(url):
    response = request.urlopen(url)
    html = response.read()
    data = html.decode('utf-8')
    soup = BeautifulSoup(data)
    list_img = []
    for list in soup.find_all("img", {"class", "BDE_Image"}):
        list_img.append(list.attrs["src"])
    return list_img

def downloadImg(list_img):
    count = 1
    for i in list_img:
        filepath = path + str(count)+".jpg"
        with open(filepath, 'wb') as file:
            print(filepath)
            image_data = request.urlopen(i).read()
            file.write(image_data)
        count += 1
def multi_thread(count, func):
    threads = []
    for i in range(0, count):
        threads.append(base_thread(func))
    for j in range(0, count):
        threads[j].start()
    for k in range(0, count):
        threads[k].join()
#CrawlerFunc("http://tieba.baidu.com/p/3764230390")
