# *args 和**kwargs
# https://stackoverflow.com/questions/21809112/what-does-tuple-and-dict-mean-in-python


# *: 输入的是位置参数,例如: 1,2 , 输出的是元组(1,2)
def args(*args):
    return args


# **输入的是命名位置参数,例如: a=1,b=2 , 输出的是字典{'a':1,'b':2}
def kwargs(**kwargs):
    return kwargs


def test_kwargs():
    v = kwargs()
    assert {} == v, 'kwargs 空参错误'

    v = kwargs(a=1, b=2)
    assert {'a': 1, 'b': 2} == v, 'kwargs 传a=1格式错误'

    param = {'a': 1, 'b': 2}
    # **: 输入的是字典, 输出的是命名位置参数: a=1,b=2
    v = kwargs(**param)
    assert {'a': 1, 'b': 2} == v, 'kwargs 传字典错误'


def test_args():
    v = args()
    assert () == v, 'args 空参数错误'

    v = args(1, 2)
    assert (1, 2) == v, 'args 1 tuple error'

    params = (1, )
    # *: 输入的是序列, 输出的是位置参数, 1,2,
    v = args(*params)
    assert (1, ) == v, 'args 1 tuple error'

    params = (1, 2, 3)
    v = args(*params)
    assert (1, 2, 3) == v, 'args 3 tuple error'

    params = [1, 2, 3]
    v = args(*params)
    assert (1, 2, 3) == v, 'args 3 list error'

    # set 也可以用set((1,2,3))初始化
    params = {1, 2, 3}
    v = args(*params)
    assert (1, 2, 3) == v, 'args 3 set error'

    params = range(1, 4)
    v = args(*params)
    assert (1, 2, 3) == v, 'args range(1,4) error'

    params = 'a'
    v = args(*params)
    assert ('a', ) == v, 'args 1 str error'

    params = 'a', 'b'
    v = args(*params)
    assert ('a', 'b') == v, 'args 1 str error'
