# 增删改查
# in, enumerate
# setdefault,update,get,pop,popitem
# sort
# 浅复制 和 深度复制
# 方法：dict(p)
import copy


def test_1():
    # 增删改查
    dict1 = {'a': 1, 'b': 2}
    dict1['c'] = 3
    assert {'a': 1, 'b': 2, 'c': 3} == dict1, 'dict 新增失败'

    del dict1['b']
    assert {'a': 1, 'c': 3} == dict1, 'dict 删除失败'
    dict1['c'] = 4
    assert {'a': 1, 'c': 4} == dict1, 'dict 修改失败'

    c = dict1['c']
    assert 4 == c, 'dict 查询失败'
    pass


def test_2():
    # in, enumerate
    dict1 = {'a': 1, 'b': 2}
    indexs = [i for i, v in enumerate(dict1.items()) if v[0] == 'b']
    assert [1] == indexs, 'dict enumerate error'

    assert 'a' in dict1, 'dict in error'
    pass


def test_3():
    # setdefault,update,get,pop,popitem
    # setdefault 如果有没则增加，有则不变
    dict1 = {'a': 1, 'b': 2}
    dict1.setdefault('c', 4)
    assert {'a': 1, 'b': 2, 'c': 4}, 'dict setdefault error'

    dict1.setdefault('b', 1)
    assert {'a': 1, 'b': 2, 'c': 4} == dict1, 'dict setdefault b error'

    dict1.update({'c': 5})
    assert {'a': 1, 'b': 2, 'c': 5} == dict1, 'dict update error'

    c = dict1.get('c', 1)
    assert 5 == c, 'dict get error'

    f = dict1.get('f', 1)
    assert 1 == f, 'dict get f error'

    dict1.pop('c')
    assert {'a': 1, 'b': 2} == dict1, 'dict pop error'

    dict1.popitem()
    assert {'a': 1} == dict1, 'dict popitem error'

    pass


def test_4():
    # sort
    dict1 = {'b': 2, 'a': 1}
    dict2 = dict(sorted(dict1.items(), key=lambda kv: kv[0]))
    assert {'a': 1, 'b': 2} == dict2, 'dict sorted 1 error'

    dict1 = {'b': 2, 'a': 1, 'c': 1}
    dict2 = dict(sorted(dict1.items(), key=lambda kv: (kv[1], kv[0])))
    assert {'a': 1, 'c': 1, 'b': 2}

    pass


def test_5():
    # 浅复制 和 深度复制
    # 1.浅复制：不改变原字典
    dict1 = {'a': 1, 'b': 2}
    dict2 = dict1.copy()
    dict2.update({'b': 1})
    assert {'a': 1, 'b': 2} == dict1, 'dict copy 1 error'
    assert {'a': 1, 'b': 1} == dict2, 'dict copy 1.1 error'

    # 2.浅复制：改变原字典--子对象
    dict1 = {'a': 1, 'b': {'c': 1}}
    dict2 = dict1.copy()
    dict2['b'].setdefault('d', 2)
    assert {'a': 1, 'b': {'c': 1, 'd': 2}} == dict1, 'dict copy 2 error'
    assert {'a': 1, 'b': {'c': 1, 'd': 2}} == dict2, 'dict copy 2.1 error'

    # 3.浅复制：不改变原字典
    dict1 = {'a': 1, 'b': {'c': 1}}
    dict2 = copy.deepcopy(dict1)
    dict2['b'].setdefault('d', 2)
    assert {'a': 1, 'b': {'c': 1}} == dict1, 'dict copy 3 error'
    assert {'a': 1, 'b': {'c': 1, 'd': 2}} == dict2, 'dict copy 3.1 error'

    pass


def test_6():
    # 方法：dict(p)
    dict1 = dict()
    assert {} == dict1, 'dict new 1 error'

    dict1 = dict({'a': 1})
    assert {'a': 1} == dict1, 'dict new 2 error'

    dict1 = dict([('a', 1), ('b', 2)])
    assert {'a': 1, 'b': 2} == dict1, 'dict new 3 error'

    dict1 = dict(a=1, b=2)
    assert {'a': 1, 'b': 2} == dict1, 'dict new 4 error'

    params = {'a': 1, 'b': 2}
    dict1 = dict(**params)
    assert {'a': 1, 'b': 2} == dict1, 'dict new 5 error'
    pass
