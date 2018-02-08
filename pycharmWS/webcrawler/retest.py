import re
pat = re.compile('A')
m = pat.search('CBA')
# print(m)                                    # <_sre.SRE_Match object; span=(2, 3), match='A'> (这是一个 MatchObject)

m = pat.search('CBD')
# print(m)                                    # None

m = re.search('asd','ASDasd')   # 第一个参数是 匹配规则，第二个参数是 要匹配的字符串
# print(m)                                      # <_sre.SRE_Match object; span=(3, 6), match='asd'>

m = re.search('asd','BSDbsd')
# print(m)                                      # None

m = re.split(",","a,bc,def,ghij")  # 以逗号（,）进行分割
# print(m)                                        # ['a', 'bc', 'def', 'ghij']

pat = re.compile('[A-Z]+')           # 匹配大写字母（连续的一起）
m = pat.findall('ASDcDFGAa')
# print(m)                                           # ['ASD', 'DFGA']

print(re.match('www','www.runob.com').span())
print(re.match('com','www.runob.com'))

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchObj:
    print('matchObj.group() : ',matchObj.group())
    # print('matchObj.group(0) : ',matchObj.group(0))
    print('matchObj.group(1) : ',matchObj.group(1))
    print('matchObj.group(2) : ',matchObj.group(2))
    # print('matchObj.group(3) : ',matchObj.group(3))
else:
    print("NO match")





