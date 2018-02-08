# -*- encoding: UTF-8 -*-
import requests
import re,time
from bs4 import BeautifulSoup
import os,json
import Crypto.Cipher
from pprint import pprint

Defaulf_Header = {'Referer': 'http://music.163.com/',
                  'Host': 'music.163.com',
                  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
                  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                  'Accept-Encoding': 'gzip, deflate'
                  }

BASE_URL = 'http://music.163.com'

_session = requests.session()
_session.headers.update(Defaulf_Header)

def getPage(pageIndex):
    pageUrl = 'http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset='+pageIndex
    soup = BeautifulSoup(_session.get(pageUrl).content)
    