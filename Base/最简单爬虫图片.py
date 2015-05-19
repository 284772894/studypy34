import urllib.request as request
from bs4 import BeautifulSoup
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
#https://pypi.python.org/pypi/BeautifulSoup/3.2.1
def CrawlerFunc(url):
    response = request.urlopen(url)  
    html = response.read()  
    data = html.decode('utf-8')
    soup = BeautifulSoup(data)  
    path = 'e:/apps/pic/'
    count = 1
    list_img = []
    for list in soup.find_all("img", {"class", "BDE_Image"}):
        list_img.append(list.attrs["src"])
    for i in list_img:
        filepath = path + str(count)+".jpg"
        with open(filepath, 'wb') as file:
            print(filepath)
            image_data = request.urlopen(i).read()
            file.write(image_data)
        count += 1
#CrawlerFunc("http://tieba.baidu.com/p/3764230390")
