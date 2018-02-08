from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import HTTPError

html = urlopen('http://pythonscraping.com/pages/page1.html')
bsObj = BeautifulSoup(html.read(), "lxml")
print(bsObj.h1, bsObj.nonExistentTag)

try:
    html2 = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # 返回空值，中断程序，或者执行另一个方案
else:
    print(html2.read())
    # 程序继续。注意：如果在上面的代码块执行了 break 或代码返回，
    # 那么就不需要 else 语句了

print('############################################################')


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj2 = BeautifulSoup(html.read(), "lxml")
        title = bsObj2.body.h1
    except AttributeError as e:
        print(e)
        return None
    else:
        return title


title = getTitle("http://pythonscraping.com/pages/page1.html")
print(title)

print("###############################################################")
html3 = urlopen("http://pythonscraping.com/pages/warandpeace.html")
# print(html3.read())
bsObj2 = BeautifulSoup(html3,"lxml")
# namelist = bsObj2.findAll("span", {"class": "green"})     # 把绿色的字（即人名）都找出来
# for name in namelist:
#     print(name.get_text())
namelist = bsObj2.findAll(text="The prince")                        # 把文字都找出来
print(len(namelist))
