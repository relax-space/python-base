# 增删改查，discard,
# - | & ^, difference,union,intersection,symmetric_difference
# 方法：set(p),  in,enumerate
# sorted
# 浅复制 和 深度复制

import copy

# pytest -vs cainiao1/test_set.py


def test_1():
    # 增删改查，discard,
    set1 = {1, 2}
    set1.add(3)
    assert {1, 2, 3} == set1, 'add error'

    set1.remove(2)
    assert {1, 3} == set1, 'remove error'

    set1.update({1, 4})
    assert {1, 3, 4} == set1, 'update 1 error'

    set1.update((5,))
    assert {1, 3, 4, 5} == set1, 'update 2 error'

    e = 5 if 5 in set1 else None
    assert e == 5, 'in error'

    set1.discard(5)
    assert {1, 3, 4} == set1, 'discart error'
    pass


def test_2():
    # - | & ^, difference,union,intersection,symmetric_difference
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    setx = set1-set2
    assert {1} == setx, '- error'

    setx = set1 | set2
    assert {1, 2, 3, 4} == setx, '| error'

    setx = set1 & set2
    assert {2, 3} == setx, '& error'

    setx = set1 ^ set2
    assert {1, 4} == setx, '^ error'

    setx = set1.difference(set2)
    assert {1} == setx, '- error'

    setx = set1.union(set2)
    assert {1, 2, 3, 4} == setx, '| error'

    setx = set1.intersection(set2)
    assert {2, 3} == setx, '& error'

    setx = set1.symmetric_difference(set2)
    assert {1, 4} == setx, '^ error'

    pass


def test_3():
    # 方法：set(p),  in,enumerate
    set1 = set([1, 2])
    assert {1, 2} == set1, '[1,2] error'

    set1 = set((1,))
    assert {1} == set1, r'{1} error'

    set1 = set('abc')
    assert {'a', 'b', 'c'} == set1, 'abc error'

    set_indexs = [i for i, v in enumerate(set1)]
    assert [0, 1, 2] == set_indexs, 'enumerate error'
    pass


def test_4():
    # sorted
    set1 = {'b', 'a', 'c'}
    sorted(set1)
    assert {'a', 'b', 'c'} == set1, 'sorted error'
    pass


class Person:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    pass


def test_5():
    # 浅复制 和 深度复制
    set1 = {1,  Person(2, 3)}
    set2 = {i for i in set1}
    set2.update({4})
    assert not {4}.issubset(set1), 'copy 1 error'
    assert {4}.issubset(set2), 'copy 2 error'

    set2 = set1.copy()
    for i in set2:
        if type(i) == Person:
            i.a = 4
    p1: Person = [i for i in set1 if type(i) == Person][0]
    p2: Person = [i for i in set2 if type(i) == Person][0]

    assert 4 == p1.a, 'copy 3 error'
    assert 4 == p2.a, 'copy 4 error'


    set1 = {1,  Person(2, 3)}
    set2 = copy.deepcopy(set1)
    for i in set2:
        if type(i) == Person:
            i.a = 4
    p3: Person = [i for i in set1 if type(i) == Person][0]
    p4: Person = [i for i in set2 if type(i) == Person][0]

    assert 2 == p3.a, 'copy 3 error'
    assert 4 == p4.a, 'copy 4 error'

    pass
