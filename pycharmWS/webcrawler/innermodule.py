from datetime import  datetime

now = datetime.now()
print(now)
print(type(now))
print(now.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t))


# 2017-12-27 17:41:00.517086
# <class 'datetime.datetime'>
# 1514367660.517086
# 2015-04-19 12:20:00
