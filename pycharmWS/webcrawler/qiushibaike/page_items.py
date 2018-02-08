import re
from urllib import request
from webcrawler.qiushibaike.tools import Tools

class PageItems(object):
    def __init__(self,page = None):
        self.page = page

    def get_page_dict_item(self):
        if self.page is None:
            return None
        try:
            url = "https://www.qiushibaike.com/hot/page/"+ str(self.page)
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"
            }
            req = request.Request(url,headers = headers)
            response = request.urlopen(req)
            html = response.read().decode('utf-8')
            pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>',re.S)
            items = re.findall(pattern, html)
            for item in items:
                # Tools.log(item)
                print(Tools.wash_off_html_tag(item[0])+"\n")
                print(Tools.wash_off_html_tag(item[1]))

        except BaseException as e:
            print(str(e))
            return None

pageItem = PageItems(1)
pageItem.get_page_dict_item()
