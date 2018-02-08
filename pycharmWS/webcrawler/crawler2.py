# -*- coding: UTF-8 -*-
from urllib import request
import chardet
# import sys
# print("====================== import mode =========================")
# print("The command line arguments are:")
# for i in sys.argv:
#     print(i)
# print("\n The Python path are: ", sys.path)
#
# from sys import argv, path
# print("====================== from import =========================")
# print("path:", path)

# The Python path are:
# ['F:\\pycharmWS\\webcrawler', 'F:\\pycharmWS', 'F:\\python35\\python35.zip', 'F:\\python35\\DLLs',
#  'F:\\python35\\lib', 'F:\\python35', 'F:\\python35\\lib\\site-packages']
# ====================== from import =========================
# path: ['F:\\pycharmWS\\webcrawler', 'F:\\pycharmWS', 'F:\\python35\\python35.zip', 'F:\\python35\\DLLs',
# 'F:\\python35\\lib', 'F:\\python35', 'F:\\python35\\lib\\site-packages']

# if __name__ == "__main__":
#     req = request.Request("http://fanyi.baidu.com")
#     response = request.urlopen(req)
#     html = response.read()
#     charset = chardet.detect(html)
#     print(charset)

if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com")
    response = request.urlopen(req)
    print("================ url : ", response.geturl())
    print("================ responseInfo : ", response.info())
    print("================ responseCode : ", response.getcode())