# *args 和**kwargs


def args(*args):
    return args


def kwargs(**kwargs):
    return kwargs


def test_kwargs():
    v = kwargs()
    assert {} == v, 'kwargs 空参错误'

    param = {'a': 1, 'b': 2}
    v = kwargs(**param)

    assert {'a': 1, 'b': 2} == v, 'kwargs 传字典错误'

    v = kwargs(a=1, b=2)
    assert {'a': 1, 'b': 2} == v, 'kwargs 传a=1格式错误'


def test_args():
    v = args()
    assert () == v, 'args 空参数错误'

    params = (1,)
    v = args(*params)
    assert (1,) == v, 'args 1 tuple error'

    params = (1, 2, 3)
    v = args(*params)
    assert (1, 2, 3) == v, 'args 3 tuple error'

    params = [1, 2, 3]
    v = args(*params)
    assert (1, 2, 3) == v, 'args 3 list error'

    params = set((1, 2, 3))
    v = args(*params)
    assert (1, 2, 3) == v, 'args 3 set error'

    params = range(1, 4)
    v = args(*params)
    assert (1, 2, 3) == v, 'args range(1,4) error'

    params = 'a'
    v = args(*params)
    assert ('a',) == v, 'args 1 str error'

    params = 'a', 'b'
    v = args(*params)
    assert ('a', 'b') == v, 'args 1 str error'
