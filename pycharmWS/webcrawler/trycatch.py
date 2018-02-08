import logging
try:
    print('try result..')
    result = 10 / 2
    print('result : ',result)
except ZeroDivisionError as e:                                            # 如果发生错误，则被捕获，捕获后则行里面的代码
    print('Zero Division Error',e)
except ValueError as e:
    print('Value Error',e)
else:                                                                                       # 无错误
    print('如果没有错误则执行 else 里面的语句')
finally:                                                                                  # 一定会执行
    print('Finally')

############################################################################################

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        result = bar('2')
        print(result)
    except Exception as e:
        logging.exception(e)                                                        # import 了 logging 包，logging包内置了这个函数
    finally:
        print('finally')

main()

####################################### 自己抛异常 #################################################

def foo2(s):
    n = int(s)
    if n == 0 :
        raise ValueError('invalid value : %s'%s)
    return 10/n

def bar2(s):
    try:
        foo2(s)
    except ValueError as e:
        print("ValueError",ValueError)
        raise


bar2('0')
