'''

说明：使用装饰器 和 不使用装饰器的效果
概念：装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。 装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象。
理解：装饰器@的理解：@req_deco等价于req_2=req_deco(req2)
'''
from functools import wraps


def req_1():
    print(1)


def req_deco(f):
    # @wraps(f),为了方便理解，这个暂时去了，实际用的时候要加上，作用就是加上后req_2.__name__的结果是req_2,不加返回的结果是wrap
    def wrap():
        print(2)
        f()
        print(3)
        return 4
    return wrap


@req_deco
def req_2():
    print(1)


deco = req_deco(req_1)
print(deco())
print('==========')
print(req_2())

'''
输出：
2
1
3
4
==========
2
1
3
4
'''
