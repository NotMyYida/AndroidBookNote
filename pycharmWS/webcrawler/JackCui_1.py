from urllib import request

import chardet

response = request.urlopen("http://fanyi.baidu.com")
html = response.read()
# html = html.decode("utf-8")
# print(html)

charset = chardet.detect(html)
print(charset)

requestUrl = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
