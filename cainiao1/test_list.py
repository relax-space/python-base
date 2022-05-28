# 增删改查，insert,pop
# 方法：list(p), + , in,enumerate
# append 和 extend
# list.index(obj),sort
# 浅复制 和 深度复制
# 倒序删除

import copy

#  pytest -vs  .\cainiao1\test_list.py


def test_1():
    # 增删改查，增和删
    list1 = ['a', 'b', 'c']
    list1.append('d')
    assert ['a', 'b', 'c', 'd'] == list1, 'append error'
    del list1[0]
    assert ['b', 'c', 'd'] == list1, 'del error'
    list1[0] = 'e'
    assert ['e', 'c', 'd'] == list1, 'update error'
    c = list1[1]
    assert 'c' == c, 'query error'

    list1.insert(1, 'f')
    assert ['e', 'f', 'c', 'd'] == list1, 'insert error'
    list1.pop(1)
    assert ['e', 'c', 'd'] == list1, 'pop error'
    list1.pop()
    assert ['e', 'c'] == list1, 'pop 2 error'


def test_2():
    # 方法：list(p), + , in,enumerate
    list1 = list('abc')
    assert ['a', 'b', 'c'] == list1, 'list(p) 方法错误'
    list1 = list1 + ['d', 'e']
    assert ['a', 'b', 'c', 'd', 'e'] == list1, 'list相加错误'
    assert 'a' in list1, 'list的in操作错误'

    list2 = list({'name': 'a', 'age': 19})
    assert ['name', 'age'] == list2, 'list(p) 方法错误'

    indexs = [i for i, _ in enumerate(list2)]
    assert [0, 1] == indexs, 'enumerate error'


def test_3():
    # append 和 extend
    list1 = ['a', 'b', 'c']
    list2 = ['d', 'e']
    list_append = list1.copy()
    list_append.append(list2)
    assert ['a', 'b', 'c', ['d', 'e']] == list_append, 'list append方法错误'
    list_extend = list1.copy()
    list_extend.extend(list2)
    assert ['a', 'b', 'c', 'd', 'e'] == list_extend, 'list extentd 方法错误'


def test_4():
    # list.index(obj),sort
    list1 = ['b', 'c', 'a']
    i = 0
    for v in list1:
        assert list1.index(v) == i, f'list index方法错误 i:{i},v:{v}'
        i += 1

    list1.sort()
    assert ['a', 'b', 'c'] == list1, 'list sort 方法错误'
    list1.sort(reverse=True)
    assert ['c', 'b', 'a'] == list1, 'list sort reverse 方法错误'

    list2 = [{
        'name': 'b',
        'age': 20
    }, {
        'name': 'a',
        'age': 18
    }, {
        'name': 'b',
        'age': 19
    }]
    list2.sort(key=lambda kv: kv['name'])
    assert {'name': 'a', 'age': 18} == list2[0], 'list sort key方法错误'
    list2.sort(key=lambda kv: kv['age'])
    assert [{
        'name': 'a',
        'age': 18
    }, {
        'name': 'b',
        'age': 19
    }, {
        'name': 'b',
        'age': 20
    }] == list2, 'list sort key 方法错误'
    list2.sort(key=lambda kv: (kv['name'], kv['age']))
    assert [{
        'name': 'a',
        'age': 18
    }, {
        'name': 'b',
        'age': 19
    }, {
        'name': 'b',
        'age': 20
    }] == list2, 'list sort key 方法错误'


def test_5():
    # 浅复制 和 深度复制
    # 只有list1中的数据是引用类型的时候，才会考虑deepcopy，否则，平常的copy就行
    list1 = ['a', 'b', 'c', ['e', 'f']]
    list2 = list1
    list3 = list1[:]
    list4 = list1.copy()
    list5 = [i for i in list1]
    list6 = copy.deepcopy(list1)

    assert id(list1) == id(list2), '== error'
    assert id(list1) != id(list3), '[:] error'
    assert id(list1) != id(list4), 'list copy error'
    assert id(list1) != id(list5), 'for error'
    assert id(list1) != id(list6), 'deepcopy error'

    list6[3][0] = 'd'
    assert ['a', 'b', 'c', ['e', 'f']] == list1, 'deepcopy 1 error'
    assert ['a', 'b', 'c', ['d', 'f']] == list6, 'deepcopy 2 error'


def test_6():
    list1 = ['a', 'b', 'c', 'd']
    for i in range(len(list1) - 1, -1, -1):
        if list1[i] == 'c':
            del list1[i]
    assert ['a', 'b', 'd'] == list1, 'list delete error'


def test_7():
    # 不要这样删除:https://blog.51cto.com/u_14246112/3157689
    list1 = ['a', 'b', 'c']
    for i in list1:
        list1.remove(i)
    # 本意是删除所有元素,但是删除的过程中列表发生了位移,所以删除了 a和c
    assert ['b'] == list1, 'list delete 2 error'


def test_8():
    a1 = [i for i in range(100)]
    s1 = split_list_by_size(a1, 7)
    # 每个小集合应该都是7,最后一个是小于等于7
    assert len(s1[-1]) <= 7, 'split size 1 error'
    s1.pop()
    for i in s1:
        assert len(i) == 7, 'split size 2 error'


def test_9():
    a1 = [i for i in range(100)]
    s1 = split_list_by_number(a1, 7)
    # 大集合中有7个小集
    assert len(s1) == 7, 'split number 2 error'


def split_list_by_size(raw_list, n):
    # n:小集合的长度为n
    l = len(raw_list)
    return [raw_list[i:i + n] for i in range(0, l, n)]


def split_list_by_number(raw_list, n):
    # n:有多少个小集合的长度为
    l = len(raw_list)
    s = int(l / n) + 1
    return [raw_list[i:i + s] for i in range(0, l, s)]
