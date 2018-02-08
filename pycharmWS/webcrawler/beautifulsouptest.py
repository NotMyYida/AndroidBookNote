# -*- coding: utf-8 -*-
import bs4
from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'lxml')
# find = soup.find('p')
# print("find's return type is ", type(find))
# print("find's content is ", find)
# print("find's tag name is ", find.name)
# print("find's Attribute(class) is ", find['class'])
# print("find's navigable string is ", find.string)

# soup.p # 查找第一个 p 标签
# soup.head # 查找第一个 head 标签

# for child in soup.body.children:
#     print(child)
#
# print('----------------------------------')
#
# for parent in soup.p.parent:
#     print(parent)

# for brother in soup.a.next_siblings:
#     print(brother)
#
# print('***********************************************************')
#
# for preBrother in soup.a.previous_siblings:
#     print(preBrother)

##########################################################################
#                                                                        #
#                                 split                                  #
#                                                                        #
##########################################################################
# markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
# soup = BeautifulSoup(markup, 'lxml')
# comment = soup.b.string
# print(comment)
# if type(comment) == bs4.element.Comment :
#     print('该字符是注释')
# else:
#     print('该字符不是注释')

# allTitle = soup.find_all('title')
# [<title>The Dormouse's story</title>]
# allPTitle = soup.find_all('p', 'title')
# [<p class="title"><b>The Dormouse's story</b></p>]
# allA = soup.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# idLink2 = soup.find_all(id='link2')
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
soup.find(string=re.compile('sisters'))
