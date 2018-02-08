
def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])                 # 高阶函数 将函数f 传入进去
l = list(r)
print(l)


from functools import reduce
def add(x,y):
        return x + y

def mul(x,y):
    return x * y

print(reduce(mul,[1,3,5,7,9]))                                                  # reduce 函数

def is_odd(num):
    return num % 2 == 1

odds = filter(is_odd,[1,2,3,4,5,6,7,8])                                     # filter 求奇数
o = list(odds)
print(o)