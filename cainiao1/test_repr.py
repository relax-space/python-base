
'''
说明: repr是可以用eval转换回对象, str不能

其他文档: https://www.cnblogs.com/miaoning/p/11399575.html

__str__是一个对象的非正式的、易于阅读的字符串描述，当类str实例化（ str(object) ）时会被调用，
以及会被内置函数format()和print()调用；__repr__是一个对象的官方的字符串描述，
会被内置函数repr()方法调用，它的描述必须是信息丰富的和明确的。
也就是说__str__返回的结果可读性强，__repr__返回的结果更加准确

'''
import datetime


def test_repr1():
    a = datetime.datetime.now()
    assert eval(repr(a)) == a, 'repr error'
    assert eval(str(a)) != a, 'str error'
