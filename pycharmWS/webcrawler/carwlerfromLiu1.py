import ssl
from urllib.request import Request
from urllib.request import urlopen

context = ssl._create_unverified_context()

# HTTP 请求
request = Request(url = "https://foofish.net/pip.html",
                                method="GET",
                                headers={"Host": "foofish.net"},
                                data=None)


# HTTP响应
# response = urlopen(request,context = context)
# headers = response.info()                                                                           #请求头
# content = response.read()                                                                           #响应体
# code = response.getcode()                                                                          #状态码

# print("headers : %s \n content : %s \n code : %s "%(headers,content,code))
# headers : Server: nginx/1.10.2
# Date: Tue, 02 Jan 2018 03:54:43 GMT
# Content-Type: text/html
# Content-Length: 12114
# Last-Modified: Mon, 01 Jan 2018 23:50:21 GMT
# Connection: close
# Vary: Accept-Encoding
# ETag: "5a4ac93d-2f52"
# Strict-Transport-Security: max-age=15768000
# Accept-Ranges: bytes
#
#
#  content : b'<!DOCTYPE html>\n<html lang="zh-cmn-hans">\n    <head>\n        <meta charset="utf-8">\n        <meta http-equiv="X-UA-Compatible" content="IE=edge">\n        <meta name="viewport" content="width=device-width, initial-scale=1">\n        <meta name="description" content="\xe5\x9c\xa8 python \xe4\xb8\xad\xe7\x94\xa8pip\xe5\xae\x89\xe8\xa3\x85\xe4\xbe\x9d\xe8\xb5\x96\xe5\x8c\x85\xe6\x97\xb6\xe9\xbb\x98\xe8\xae\xa4\xe4\xbc\x9a\xe4\xbb\x8e https://pypi.python.org/simple/\xe8\xbf\x99\xe4\xb8\xaa\xe5\x9c\xb0\xe5\x9d\x80\xe5\x8f\x96\xe4\xb8\x8b\xe8\xbd\xbd\xef\xbc\x8c\xe4\xbd\x86\xe6\x98\xaf\xe8\xbf\x99\xe4\xb8\xaa\xe7\xbd\x91\xe7\xab\x99\xe7\xbb\x8f\xe5\xb8\xb8\xe5\x87\xba\xe7\x8e\xb0\xe4\xb8\x8b\xe8\xbd\xbd\xe4\xb8\x8d\xe7\xa8\xb3\xe5\xae\x9a\xe3\x80\x81\xe8\xae\xbf\xe9\x97\xae\xe9\x80\x9f\xe5\xba\xa6\xe9\x9d\x9e\xe5\xb8\xb8\xe6\x85\xa2\xe7\x9a\x84\xe6\x83\x85\xe5\x86\xb5\xef\xbc\x8c\xe8\xbf\x99\xe6\x97\xb6\xef\xbc\x8c\xe6\x88\x91\xe4\xbb\xac\xe5\x8f\xaf\xe4\xbb\xa5\xe4\xbf\xae\xe6\x94\xb9\xe9\x85\x8d\xe7\xbd\xae\xe7\x94\xa8\xe5\x9b\xbd\xe5\x86\x85\xe5\x8e\x82\xe5\x95\x86\xe6\x8f\x90\xe4\xbe\x9b\xe7\x9a\x84\xe9\x95\x9c\xe5\x83\x8f\xe5\x9c\xb0\xe5\x9d\x80\xe6\x9d\xa5\xe6\x9b\xbf\xe6\x8d\xa2\xef\xbc\x8c\xe4\xb8\x80\xe4\xb8\xaa\xe6\x98\xaf\xe8\xb1\x86\xe7\x93\xa3\xe7\x9a\x84\xe9\x95\x9c\xe5\x83\x8f\xef\xbc\x8c\xe5\x8f\xa6\xe4\xb8\x80\xe4\xb8\xaa\xe6\x98\xaf\xe4\xb8\xad\xe5\x9b\xbd\xe7\xa7\x91\xe5\xad\xa6\xe6\x8a\x80\xe6\x9c\xaf\xe5\xa4\xa7\xe5\xad\xa6\xe7\x9a\x84\xe3\x80\x82\xe5\x9c\xb0\xe5\x9d\x80\xe5\x88\x86\xe5\x88\xab\xe6\x98\xaf\xef\xbc\x9a \xe8\xb1\x86\xe7\x93\xa3\xef\xbc\x9ahttp://pypi.douban.com/ \xe4\xb8\xad\xe5\x9b\xbd\xe7\xa7\x91\xe5\xad\xa6\xe6\x8a\x80\xe6\x9c\xaf\xe5\xa4\xa7\xe5\xad\xa6 ...">\n        <meta name="keywords" content="pip">\n\n\n\n        <link rel="icon" href="https://foofish.net/favicon.ico">\n        <link rel="canonical" href="https://foofish.net/pip.html"/>\n        <title>\xe4\xbf\xae\xe6\x94\xb9Python\xe7\x9a\x84pip\xe5\xae\x89\xe8\xa3\x85\xe6\xba\x90 - FooFish-Python\xe4\xb9\x8b\xe7\xa6\x85</title>\n\n        <!-- Stylesheets -->\n        <link href="https://foofish.net/theme/css/bootstrap.min.css" rel="stylesheet">\n        <link href="https://foofish.net/theme/css/fonts.css" rel="stylesheet">\n        <link href="https://foofish.net/theme/css/nest.css" rel="stylesheet">\n        <link href="https://foofish.net/theme/css/pygment.css" rel="stylesheet">\n        <!-- /Stylesheets -->\n\n        <!-- RSS Feeds -->\n        <link href="https://foofish.net/feeds/all.atom.xml" type="application/atom+xml" rel="alternate" title="FooFish-Python\xe4\xb9\x8b\xe7\xa6\x85 Full Atom Feed" />\n        <link href="https://foofish.net/feeds/rss.xml" type="application/rss+xml" rel="alternate" title="FooFish-Python\xe4\xb9\x8b\xe7\xa6\x85 Full RSS Feed" />\n        <!-- /RSS Feeds -->\n\n        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->\n        <!--[if lt IE 9]>\n          <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>\n          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>\n        <![endif]-->\n\n        <!-- Google Analytics -->\n        <script>\n          (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n          })(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');\n\n          ga(\'create\', \'UA-42613705-2\', \'auto\');\n          ga(\'send\', \'pageview\');\n        </script>\n        <!-- /Google Analytics -->\n\n\n        <script type=\'text/javascript\'>\n          var _vds = _vds || [];\n          window._vds = _vds;\n          (function(){\n            _vds.push([\'setAccountId\', \'8c242d1b98c50c29\']);\n            (function() {\n              var vds = document.createElement(\'script\');\n              vds.type=\'text/javascript\';\n              vds.async = true;\n              vds.src = (\'https:\' == document.location.protocol ? \'https://\' : \'http://\') + \'dn-growing.qbox.me/vds.js\';\n              var s = document.getElementsByTagName(\'script\')[0];\n              s.parentNode.insertBefore(vds, s);\n            })();\n          })();\n      </script>\n\n    </head>\n\n    <body>\n\n        <!-- Header -->\n    <div class="header-container" style="background: linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2)), url(\'https://foofish.net/images/peitu/jacob-repko-64098.jpg\'); background-position: center; background-size: cover;">\n\n            <!-- Static navbar -->\n            <div class="container">\n                <div class="header-nav">\n                    <div class="header-logo">\n                        <a class="pull-left" href="https://foofish.net/">\n                            FooFish-Python\xe4\xb9\x8b\xe7\xa6\x85\n                        </a>\n                    </div>\n                    <div class="nav pull-right">\n                                <a href="https://foofish.net/">\xe9\xa6\x96 \xe9\xa1\xb5</a>\n                                <a href="https://foofish.net/categories.html">\xe5\x88\x86 \xe7\xb1\xbb</a>\n                                <a href="https://foofish.net/tags.html">\xe6\xa0\x87 \xe7\xad\xbe</a>\n                            <a  href="https://foofish.net/pages/about.html">\xe5\x85\xb3\xe4\xba\x8e</a>\n                    </div>\n                </div>\n            </div>\n            <!-- /Static navbar -->\n\n            <!-- Header -->\n    <!-- Header -->\n    <div class="container header-wrapper">\n        <div class="row">\n              <div class="col-lg-12">\n                  <div class="header-content">\n                      <h1 class="header-title">\xe4\xbf\xae\xe6\x94\xb9Python\xe7\x9a\x84pip\xe5\xae\x89\xe8\xa3\x85\xe6\xba\x90</h1>\n                      <p class="header-date">By <a href="https://foofish.net/author/liuzhijun.html">liuzhijun</a>, 2015-11-23, \xe5\x88\x86\xe7\xb1\xbb\xef\xbc\x9a <a href="https://foofish.net/category/pythonji-zhu.html">Python\xe6\x8a\x80\xe6\x9c\xaf</a></p>\n                      <div class="header-underline"></div>\n                      <div class="clearfix"></div>\n                      <p class="pull-right header-tags">\n                          <span class="glyphicon glyphicon-tags mr5" aria-hidden="true"></span>\n<a href="https://foofish.net/tag/pip.html">pip</a>                      </p>\n                  </div>\n              </div>\n        </div>\n    </div>\n    <!-- /Header -->\n            <!-- /Header -->\n\n        </div>\n        <!-- /Header -->\n\n\n        <!-- Content -->\n    <div class="container content">\n        <article>\n        <p>\xe5\x9c\xa8 python \xe4\xb8\xad\xe7\x94\xa8<code>pip</code>\xe5\xae\x89\xe8\xa3\x85\xe4\xbe\x9d\xe8\xb5\x96\xe5\x8c\x85\xe6\x97\xb6\xe9\xbb\x98\xe8\xae\xa4\xe4\xbc\x9a\xe4\xbb\x8e <a href="https://pypi.python.org/simple/">https://pypi.python.org/simple/</a>\xe8\xbf\x99\xe4\xb8\xaa\xe5\x9c\xb0\xe5\x9d\x80\xe5\x8f\x96\xe4\xb8\x8b\xe8\xbd\xbd\xef\xbc\x8c\xe4\xbd\x86\xe6\x98\xaf\xe8\xbf\x99\xe4\xb8\xaa\xe7\xbd\x91\xe7\xab\x99\xe7\xbb\x8f\xe5\xb8\xb8\xe5\x87\xba\xe7\x8e\xb0\xe4\xb8\x8b\xe8\xbd\xbd\xe4\xb8\x8d\xe7\xa8\xb3\xe5\xae\x9a\xe3\x80\x81\xe8\xae\xbf\xe9\x97\xae\xe9\x80\x9f\xe5\xba\xa6\xe9\x9d\x9e\xe5\xb8\xb8\xe6\x85\xa2\xe7\x9a\x84\xe6\x83\x85\xe5\x86\xb5\xef\xbc\x8c\xe8\xbf\x99\xe6\x97\xb6\xef\xbc\x8c\xe6\x88\x91\xe4\xbb\xac\xe5\x8f\xaf\xe4\xbb\xa5\xe4\xbf\xae\xe6\x94\xb9\xe9\x85\x8d\xe7\xbd\xae\xe7\x94\xa8\xe5\x9b\xbd\xe5\x86\x85\xe5\x8e\x82\xe5\x95\x86\xe6\x8f\x90\xe4\xbe\x9b\xe7\x9a\x84\xe9\x95\x9c\xe5\x83\x8f\xe5\x9c\xb0\xe5\x9d\x80\xe6\x9d\xa5\xe6\x9b\xbf\xe6\x8d\xa2\xef\xbc\x8c\xe4\xb8\x80\xe4\xb8\xaa\xe6\x98\xaf\xe8\xb1\x86\xe7\x93\xa3\xe7\x9a\x84\xe9\x95\x9c\xe5\x83\x8f\xef\xbc\x8c\xe5\x8f\xa6\xe4\xb8\x80\xe4\xb8\xaa\xe6\x98\xaf\xe4\xb8\xad\xe5\x9b\xbd\xe7\xa7\x91\xe5\xad\xa6\xe6\x8a\x80\xe6\x9c\xaf\xe5\xa4\xa7\xe5\xad\xa6\xe7\x9a\x84\xe3\x80\x82\xe5\x9c\xb0\xe5\x9d\x80\xe5\x88\x86\xe5\x88\xab\xe6\x98\xaf\xef\xbc\x9a</p>\n<ol>\n<li>\xe8\xb1\x86\xe7\x93\xa3\xef\xbc\x9ahttp://pypi.douban.com/</li>\n<li>\xe4\xb8\xad\xe5\x9b\xbd\xe7\xa7\x91\xe5\xad\xa6\xe6\x8a\x80\xe6\x9c\xaf\xe5\xa4\xa7\xe5\xad\xa6 http://pypi.mirrors.ustc.edu.cn/simple/ </li>\n</ol>\n<p>\xe5\x9c\xa8\xe7\x94\xa8pip\xe5\xae\x89\xe8\xa3\x85\xe7\xac\xac\xe4\xb8\x89\xe6\x96\xb9\xe5\x8c\x85\xe7\x9a\x84\xe6\x97\xb6\xe5\x80\x99\xef\xbc\x8c\xe6\x9c\x89\xe4\xb8\xa4\xe7\xa7\x8d\xe6\x96\xb9\xe5\xbc\x8f\xe4\xbd\xbf\xe7\x94\xa8\xe6\x88\x91\xe4\xbb\xac\xe8\x87\xaa\xe5\xb7\xb1\xe6\x8c\x87\xe5\xae\x9a\xe7\x9a\x84\xe9\x95\x9c\xe5\x83\x8f\xe6\xba\x90</p>\n<h3>\xe6\x89\x8b\xe5\x8a\xa8\xe6\x8c\x87\xe5\xae\x9a</h3>\n<p>\xe5\x9c\xa8 pip \xe5\x91\xbd\xe4\xbb\xa4\xe5\x90\x8e\xe9\x9d\xa2\xe7\x9b\xb4\xe6\x8e\xa5\xe6\x8c\x87\xe5\xae\x9a\xef\xbc\x8c\xe4\xbe\x8b\xe5\xa6\x82\xef\xbc\x9a</p>\n<div class="highlight"><pre><span></span><span class="n">pip</span> <span class="o">-</span><span class="n">i</span> <span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">pypi</span><span class="o">.</span><span class="n">douban</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">simple</span> <span class="n">install</span> <span class="n">Flask</span> <span class="o">--</span> <span class="n">trusted</span><span class="o">-</span><span class="n">host</span> <span class="n">pypi</span><span class="o">.</span><span class="n">douban</span><span class="o">.</span><span class="n">com</span>\n</pre></div>\n\n\n<p>\xe4\xb8\x8d\xe8\xbf\x87\xe8\xbf\x99\xe7\xa7\x8d\xe6\x96\xb9\xe5\xbc\x8f\xe5\x9c\xa8\xe6\xaf\x8f\xe6\xac\xa1\xe5\xae\x89\xe8\xa3\x85\xe6\x97\xb6\xe9\x83\xbd\xe8\xa6\x81\xe6\x89\x8b\xe5\x8a\xa8\xe6\x8c\x87\xe5\xae\x9a\xef\xbc\x8c\xe5\xbe\x88\xe9\xba\xbb\xe7\x83\xa6\xef\xbc\x8c\xe6\x89\x80\xe4\xbb\xa5\xe6\x88\x91\xe4\xbb\xac\xe5\x8f\xaf\xe4\xbb\xa5\xe4\xbd\xbf\xe7\x94\xa8\xe7\xac\xac\xe4\xba\x8c\xe7\xa7\x8d\xe6\x96\xb9\xe5\xbc\x8f</p>\n<h3>\xe5\x86\x99\xe5\x85\xa5\xe9\x85\x8d\xe7\xbd\xae</h3>\n<p>\xe6\x8a\x8a\xe9\x95\x9c\xe5\x83\x8f\xe5\x9c\xb0\xe5\x9d\x80\xe5\x86\x99\xe5\x88\xb0\xe9\x85\x8d\xe7\xbd\xae\xe6\x96\x87\xe4\xbb\xb6\xe4\xb8\xad\xef\xbc\x8c\xe5\xa6\x82\xe6\x9e\x9c\xe6\x98\xafWidnows\xe7\xb3\xbb\xe7\xbb\x9f\xef\xbc\x8c\xe9\x82\xa3\xe4\xb9\x88\xe5\x8f\xaf\xe4\xbb\xa5\xe5\x9c\xa8\xe5\xbd\x93\xe5\x89\x8d\xe7\x94\xa8\xe6\x88\xb7\xe7\x9b\xae\xe5\xbd\x95\xe4\xb8\x8b\xe9\x9d\xa2\xe5\x88\x9b\xe5\xbb\xba pip \xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9\xef\xbc\x8c\xe5\x86\x8d\xe5\x88\x9b\xe5\xbb\xba<code>pip.ini</code>\xe7\x9a\x84\xe6\x96\x87\xe4\xbb\xb6\xef\xbc\x8c\xe5\x86\x99\xe5\x85\xa5\xe5\x86\x85\xe5\xae\xb9\xef\xbc\x9a</p>\n<div class="highlight"><pre><span></span><span class="k">[global]</span>\n<span class="na">trusted-host</span> <span class="o">=</span>  <span class="s">pypi.douban.com</span>\n<span class="na">index-url</span> <span class="o">=</span> <span class="s">http://pypi.douban.com/simple</span>\n</pre></div>\n\n\n<p><img alt="pip" src="../images/pip.png" /></p>\n<p>\xe5\xa6\x82\xe6\x9e\x9c\xe6\x98\xafMac\xe6\x88\x96\xe8\x80\x85Linux\xe7\x94\xa8\xe6\x88\xb7\xef\xbc\x8c\xe5\x88\x99\xe5\x9c\xa8\xe5\xbd\x93\xe5\x89\x8d\xe7\x94\xa8\xe6\x88\xb7\xe4\xb8\x8b\xe5\x88\x9b\xe5\xbb\xba<code>.pip</code>\xe6\x96\x87\xe4\xbb\xb6\xe5\xa4\xb9</p>\n<div class="highlight"><pre><span></span>mkdir ~/.pip\n</pre></div>\n\n\n<p>\xe7\x84\xb6\xe5\x90\x8e\xe5\x9c\xa8\xe8\xaf\xa5\xe7\x9b\xae\xe5\xbd\x95\xe4\xb8\x8b\xe5\x88\x9b\xe5\xbb\xba<code>pip.conf</code>\xe6\x96\x87\xe4\xbb\xb6\xef\xbc\x8c\xe4\xb8\x80\xe6\xa0\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\x86\x85\xe5\xae\xb9\xef\xbc\x9a</p>\n<div class="highlight"><pre><span></span><span class="p">[</span><span class="k">global</span><span class="p">]</span>\n<span class="n">trusted</span><span class="o">-</span><span class="n">host</span> <span class="o">=</span>  <span class="n">pypi</span><span class="o">.</span><span class="n">douban</span><span class="o">.</span><span class="n">com</span>\n<span class="n">index</span><span class="o">-</span><span class="n">url</span> <span class="o">=</span> <span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">pypi</span><span class="o">.</span><span class="n">douban</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">simple</span>\n</pre></div>\n        <br>\n        <p align="center" >\xe5\x85\xb3\xe6\xb3\xa8\xe5\x85\xac\xe4\xbc\x97\xe5\x8f\xb7\xe3\x80\x8cPython\xe4\xb9\x8b\xe7\xa6\x85\xe3\x80\x8d\xef\xbc\x88id\xef\xbc\x9avttalk\xef\xbc\x89\xe8\x8e\xb7\xe5\x8f\x96\xe6\x9c\x80\xe6\x96\xb0\xe6\x96\x87\xe7\xab\xa0\n          <img class="weixin" alt="python\xe4\xb9\x8b\xe7\xa6\x85" src="https://foofish.net/weixin.jpg">\n        </p>\n        </article>\n\n\n\n<div class="comments">\n   \n<div id="SOHUCS" sid="pip" ></div> \n<script type="text/javascript"> \n(function(){ \nvar appid = \'cysUwE6w2\'; \nvar conf = \'prod_2d6948171cd31a746efffd8e6ae17236\'; \nvar width = window.innerWidth || document.documentElement.clientWidth; \nif (width < 960) { \nwindow.document.write(\'<script id="changyan_mobile_js" charset="utf-8" type="text/javascript" src="https://changyan.sohu.com/upload/mobile/wap-js/changyan_mobile.js?client_id=\' + appid + \'&conf=\' + conf + \'"><\\/script>\'); } else { var loadJs=function(d,a){var c=document.getElementsByTagName("head")[0]||document.head||document.documentElement;var b=document.createElement("script");b.setAttribute("type","text/javascript");b.setAttribute("charset","UTF-8");b.setAttribute("src",d);if(typeof a==="function"){if(window.attachEvent){b.onreadystatechange=function(){var e=b.readyState;if(e==="loaded"||e==="complete"){b.onreadystatechange=null;a()}}}else{b.onload=a}}c.appendChild(b)};loadJs("https://changyan.sohu.com/upload/changyan.js",function(){window.changyan.api.config({appid:appid,conf:conf})}); } })(); </script>\n\n</div>\n\n    </div>\n        <!-- /Content --> \n\n        <!-- Footer -->\n        <div class="footer gradient-2">\n            <div class="container footer-container ">\n                <div class="row">\n                    <div class="col-xs-4 col-sm-3 col-md-3 col-lg-3">\n                        <div class="footer-title">Sitemap</div>\n                        <ul class="list-unstyled">\n                            <li><a href="https://foofish.net/categories.html">\xe5\x88\x86\xe7\xb1\xbb</a></li>\n                            <li><a href="https://foofish.net/tags.html">\xe6\xa0\x87\xe7\xad\xbe</a></li>\n                            <li><a href="https://foofish.net/pages/about.html">\xe5\x85\xb3\xe4\xba\x8e</a></li>\n                            <li><a href="https://foofish.net/feeds/all.atom.xml" type="application/atom+xml" rel="alternate"></a></li>\n                            <li><a href="https://foofish.net/feeds/rss.xml" type="application/rss+xml" rel="alternate">RSS</a></li>\n                        </ul>\n                    </div>\n                    <div class="col-xs-4 col-sm-3 col-md-3 col-lg-3">\n                        <div class="footer-title">Social</div>\n                        <ul class="list-unstyled">\n                            <li><a href="https://github.com/lzjun567" target="_blank">GitHub</a></li>\n                            <li><a href="http://weibo.com/lzjun567" target="_blank">\xe5\xbe\xae\xe5\x8d\x9a</a></li>\n                            <li><a href="https://www.zhihu.com/people/zhijun-liu" target="_blank">\xe7\x9f\xa5\xe4\xb9\x8e</a></li>\n                        </ul>\n                    </div>\n                    <div class="col-xs-4 col-sm-3 col-md-3 col-lg-3">\n                        <div class="footer-title">Links</div>\n                        <ul class="list-unstyled">\n                            <li><a href="https://m.do.co/c/af4cff8f42bc" target="_blank">DigitalOcean</a></li>\n                            <li><a href="http://python.org/" target="_blank">Python.org</a></li>\n                        </ul>\n                    </div> \n                    <div class="col-xs-12 col-sm-3 col-md-3 col-lg-3">\n                        <p class="pull-right text-right">\n                            <small>&copy; foofish 2016</small>\n                        </p>\n                    </div>\n                </div>\n            </div>\n        </div>\n        <!-- /Footer -->\n    </body>\n</html>'
#  code : 200


import requests
# GET 请求
# r = requests.get("https://httpbin.org/ip")
# status_code = r.status_code
# rContent = r.content
# print(r)
# print(rContent)
# <Response [200]>
# b'{\n  "origin": "113.91.88.102"\n}\n'

# POST请求
# r2 = requests.post("https://httpbin.org/ip",data={"key":"value"})
# print(r2)
# print(r2.content)
# <Response [405]>
# b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>405 Method Not Allowed</title>\n<h1>Method Not Allowed</h1>\n<p>The method is not allowed for the requested URL.</p>\n'

# 自定义请求头
# 为了伪装成真实的浏览器，可以使用指定UA伪装成浏览器发起请求
# url = 'https://httpbin.org/headers'
# headers = {"user-agent":"Mozilla/5.0"}
# r = requests.get(url,headers = headers)
# print(r)
# print(r.content)
# <Response [200]>
# b'{\n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n    "Connection": "close", \n    "Host": "httpbin.org", \n    "User-Agent": "Mozilla/5.0"\n  }\n}\n'

# url = "http://httpbin.org/get"
# r = requests.get(url,params={"key":"val"})
# print(r.url)
# http://httpbin.org/get?key=val

# 指定 Cookie
s = requests.get("http://httpbin.org/cookies",cookies={'from-my':'browser'})
print(s.text)
# {
#   "cookies": {
#     "from-my": "browser"
#   }
# }

# r = requests.get('https://google.com',timeout = 5)
# print(r)

# 设置代理
# proxies = {
#     'http':'http://127.0.0.1:1080',
#     'https':'http://127.0.0.1:1080'
# }
#
# r = requests.get('http://www.kuaidaili.com/free/',proxies = proxies,timeout = 2)
# print(r)

# Session
s = requests.Session()
s.cookies = requests.utils.cookiejar_from_dict({"a":"c"})
r = s.get("http://httpbin.org/cookies")
print(r.text)

# {
#   "cookies": {
#     "a": "c"
#   }
# }

# r = s.get("http://httpbin.org/cookies")
# print(r.text)
