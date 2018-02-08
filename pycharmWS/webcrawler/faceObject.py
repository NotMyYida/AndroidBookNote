
class Student(object):
    pass                                                                                                            # pass 的意思是，先声明着

s = Student()                                                                                                  # 之后可以任意声明变量
s.name = 'Mike'
print(s.name)
s.age = 24
print(s.age)
s.address = 'ShenZhen'
print(s.address)

class SlotStudent(object):
    __slots__ = ('name','age')                                                                      # 限制只能有两个变量 name 和 age

s2 = SlotStudent()
s2.name = 'Jack'
s2.age = 27
print(s2.name,s.age)
s2.score = 99
print(s2.score)