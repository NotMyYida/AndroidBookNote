# -*- coding : UTF-8 -*-
from urllib import request
from urllib import parse
import json

if __name__ == "__main__":
    Request_URL = "http://fanyi.baidu.com/v2transapi"
    Form_Data = {}
    Form_Data['from'] = 'en'
    Form_Data['to'] = 'zh'
    Form_Data['query'] = 'Android'
    Form_Data['transtype'] = 'realtime'
    Form_Data['simple_means_flag'] = '3'
    # 使用urlencode方法转化为标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL, data)
    html = response.read().decode('utf-8')

    translate_result = json.load(html)
    print(translate_result[1][1])
    # translate_result = json.load(html)
    # data = translate_result["data"]
    # print(data)
  # "trans_result":{ 1
  #       "from": "en",
  #       "to": "zh",
  #       "domain": "all",
  #       "type": 2,
  #       "status": 0,
  #       "data": [ a
  #           { 2
  #               "dst": "安卓",
  #               "src": "Android",
  #               "relation": [],
  #               "result": [ b
  #                   [ c
  #                       0,
  #                       "安卓",
  #                       [ d
  #                           "0|7"
  #                       ] d,
  #                       [] d,
  #                       [ d
  #                           "0|7"
  #                       ] d,
  #                       [ d
  #                           "0|6"
  #                       ] d
  #                   ] c
  #               ]b
  #           }2
  #       ] a,
  #       "phonetic": [ a
  #           { 2
  #               "src_str": "安",
  #               "trg_str": "ān"
  #           } 2,
  #           { 2
  #               "src_str": "卓",
  #               "trg_str": "zhuó"
  #           } 2
  #       ] a
  #   } 1,
  #   "dict_result": {
  #       "edict": "",
  #       "zdict": "",
  #       "from": "kingsoft",
  #       "simple_means": {
  #           "word_name": "Android",
  #           "from": "kingsoft",
  #           "word_means": [
  #               "似人自动机",
  #               "机器人",
  #               "基于Linux平台的开源手机操作系统，主要使用于便携设备。目前尚未有统一中文名称，中国大陆地区较多人称为安卓"
  #           ],
  #           "exchange": {
  #               "word_third": "",
  #               "word_done": "",
  #               "word_pl": "",
  #               "word_est": "",
  #               "word_ing": "",
  #               "word_er": "",
  #               "word_past": ""
  #           },


