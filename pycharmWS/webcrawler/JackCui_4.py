from urllib import request
from http import cookiejar

# # 实例化一个 CookieJar 对象
# cookie = cookiejar.CookieJar()
#
# # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也叫CookieHandler
# handler = request.HTTPCookieProcessor(cookie)
#
# # 通过 CookieHandler 创建 Opener
# opener = request.build_opener(handler)
#
# response = opener.open("http://www.baidu.com")
#
# for item in cookie:
#     print('Name = %s'%item.name)
#     print('Value = %s'%item.value)

# Name = BAIDUID
# Value = D121FF8D1461D7D1A78AECDC4C3F3090:FG=1
# Name = BIDUPSID
# Value = D121FF8D1461D7D1A78AECDC4C3F3090
# Name = H_PS_PSSID
# Value = 25641_1454_21112_22160
# Name = PSTM
# Value = 1516946252
# Name = BDSVRTM
# Value = 0
# Name = BD_HOME
# Value = 0



# 保存 Cookie 到文件中
# fileName = "cookie.txt"
# cookie = cookiejar.MozillaCookieJar(fileName)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# cookie.save(ignore_discard=True, ignore_expires= True)


fileName = "cookie.txt"
cookie = cookiejar.MozillaCookieJar()
cookie.load(fileName, ignore_discard=True, ignore_expires=True)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode("utf-8"))
