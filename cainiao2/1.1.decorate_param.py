
'''
说明: req_deco1:给带参数的函数添加装饰器, req_deco2:给装饰器添加参数
'''
import time
from functools import wraps


def req_deco1(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        t1 = time.time()
        res = f(*args, **kwargs)
        print(
            f'{f.__name__}的参数:args:{args} kwargs:{kwargs}, 执行时间:{round(time.time()-t1,1)}')
        return res
    return wrap


@req_deco1
def req1(name: str, age: int):
    time.sleep(0.1)
    return f'姓名:{name}, 年龄:{age}'


def req_deco2(country: str):
    def req_deco_inner(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            t1 = time.time()
            res = f(*args, **kwargs)
            print(
                f'{f.__name__}的参数:args:{args} kwargs:{kwargs}, 执行时间:{round(time.time()-t1,1)}')
            print(f'装饰器的参数:{country}')
            return res
        return wrap
    return req_deco_inner


@req_deco2('china')
def req2(name: str, age: int):
    time.sleep(0.2)
    return f'姓名:{name}, 年龄:{age}'


if __name__ == '__main__':
    res1 = req1('肖新苗', age=18)
    print(res1)
    print('===========')
    res2 = req2('张三', age=19)
    print(res2)
