def foo(s):
    n = int(s)
    print('>>> n = %d'%n)                              # 打印出来查看
    return 10/n

print(foo('6'))


def foo2(s):
    n = int(s)
    assert  n!=0,'n is zero'                            # 如果 n==0，则抛出 AssertionError：n is zero
    return 10/n

print(foo2('2'))


import logging
logging.basicConfig(level=logging.INFO)                                           # 增加了这一句之后，多了 INFO:root:n = 0
s = '3'
n = int(s)
logging.info('n = %d'%n)
print(10/n)

# Traceback (most recent call last):
# File "F:/pycharmWS/webcrawler/trydebug.py", line 21, in <module>
#   print(10/n)
#  ZeroDivisionError: division by zero

import pdb
s = '0'
n = int(s)
pdb.set_trace()                                                         # 到这里会暂停
print(10/n)