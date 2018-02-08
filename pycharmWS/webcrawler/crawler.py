import requests #导入requests库
import beautifulsoup
r = requests.get('https://unsplash.com')
print(type(r))

#Get请求
payload = {'key1': 'value1', 'key2': 'value2'}
s = requests.get("http://httpbin.org/get", payload)
# 得到的是 http://httpbin.org/get?key1=value1&key2=value2

#Post请求
#无参数
r = requests.post('http://httpbin.org/post')
#有参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', payload)
