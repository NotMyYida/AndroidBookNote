from webcrawler.baikeandroid import url_manager,html_downloader,html_parser,html_output
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.out_put = html_output.HtmlOutput()


    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_urls():
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s "%(count,new_url))
                html_content = self.downloader.download(new_url)
                new_url, new_data = self.parser.parse(new_url, html_content, "utf-8")
                self.urls.add_new_urls(new_url)
                self.out_put.collect_data(new_data)
                if count >= 30:
                    break
                count = count + 1
            except Exception as e:
                print("craw fail "+str(e))
        self.out_put.output_html()

if __name__ == "__main__":
    rootUrl = "http://baike.baidu.com/item/Android"
    objSpider = SpiderMain()
    objSpider.craw(rootUrl)


