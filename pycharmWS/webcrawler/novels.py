import requests
from bs4 import BeautifulSoup


# 获取第一章节的内容
def getFirstChapter():
    target = "http://www.biqukan.com/1_1094/5403177.html"
    req = requests.get(url = target)
    html = req.text
    bf = BeautifulSoup(html,"lxml")
    texts = bf.find_all("div",class_="showtxt")
    print(texts[0].text.replace('\xa0'*8,'\n\n'))


# 获取章节列表
def getChapterList():
    target = 'http://www.biqukan.com/1_1094/'
    server = 'http://www.biqukan.com/'              # 服务端的地址
    req = requests.get(url = target)
    html = req.text
    div_bf = BeautifulSoup(html,"lxml")
    div = div_bf.find_all("div",class_="listmain")      # div[0]  <dd><a href="/1_1094/5621379.html">第二十一章 小纯哥哥……</a></dd>
    a_bf = BeautifulSoup(str(div[0]),"lxml")
    a = a_bf.find_all("a")
    for each in a:
        print(each.string,server + each.get('href'))

getChapterList()