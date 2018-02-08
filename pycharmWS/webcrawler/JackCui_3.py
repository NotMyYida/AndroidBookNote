from urllib import request

requestUrl = "http://www.csdn.net"
headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19"
# response = request.urlopen(requestUrl)
# req = request.Request(requestUrl,headers=headers)
# response = request.urlopen(req)
# print(response.getcode(),"\n",response.info(),'\n',response.read().decode("utf-8"))

# req.add_header("User-Agent","Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19")

# 使用代理 IP

url = "http://www.whatismyip.com.tw/"

proxy = {"http":"123.163.21.213:24758"}       # 从 http://www.xicidaili.com/ 的页面中找到的

# 创建 ProxyHandler
proxy_support = request.ProxyHandler(proxy)

# 创建 Opener
opener = request.build_opener(proxy_support)

# 安装 Opener
request.install_opener(opener)

queryIdRes = request.Request(url)
queryIdRes.add_header("User-Agent","Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19")
queryIdResponse = request.urlopen(queryIdRes)
print(queryIdResponse.read().decode("utf-8"))

