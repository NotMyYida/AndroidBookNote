from urllib.request import urlopen
from bs4 import BeautifulSoup
import re       # 正则表达式

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")
for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)

print("####################################################")

for sibling in bsObj.find("table",{"id": "giftList"}).tr.next_siblings:
    print(sibling)

print("####################################################")

print(bsObj.find("img",{"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

print("####################################################")

html2 = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj2 = BeautifulSoup(html2,"lxml")
imgs = bsObj2.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for img in imgs:
    print(img)

