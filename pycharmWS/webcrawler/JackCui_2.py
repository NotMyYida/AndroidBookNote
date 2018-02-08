from urllib import request
from urllib import parse
import json

requestUrl = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
#                       http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule           # 去掉_o
Form_data = {}
Form_data["i"] = 'Hello'
Form_data["from"] = "AUTO"
Form_data["to"] = "AUTO"
Form_data["smartresult"] = "dict"
Form_data["client"] = "fanyideskweb"
Form_data["doctype"] = "json"
Form_data["version"] = "2.1"
Form_data["keyfrom"] = "fanyi.web"
Form_data["action"] = "FY_BY_CLICKBUTTION"
Form_data["typoResult"] = "false"


data = parse.urlencode(Form_data).encode("utf-8")
response = request.urlopen(requestUrl, data)
print(response.info())
print(response.read().decode("utf-8"))

# html = response.read()
# translate_result = json.load(html)
# print(translate_result)