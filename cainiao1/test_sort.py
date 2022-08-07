from operator import itemgetter


def test_1():
    # sort
    dict1 = {'b': 2, 'a': 1}
    dict2 = dict(sorted(dict1.items(), key=lambda kv: kv[0]))
    assert {'a': 1, 'b': 2} == dict2, 'dict sorted 1 error'

    dict1 = {'b': 2, 'a': 1, 'c': 1}
    dict2 = dict(sorted(dict1.items(), key=lambda kv: (kv[1], kv[0])))
    assert {'a': 1, 'c': 1, 'b': 2}


def test_2():

    def sort1(kv):
        return kv[0]

    # sort
    dict1 = {'b': 2, 'a': 1}
    dict2 = dict(sorted(dict1.items(), key=sort1))
    assert {'a': 1, 'b': 2} == dict2, 'dict sorted 1 error'

    def sort2(kv):
        return kv[1], kv[0]

    dict1 = {'b': 2, 'a': 1, 'c': 1}
    dict2 = dict(sorted(dict1.items(), key=sort2))
    assert {'a': 1, 'c': 1, 'b': 2}


def test_3():
    # sort
    dict1 = {'b': 2, 'a': 1}
    dict2 = dict(sorted(dict1.items(), key=itemgetter(0)))
    assert {'a': 1, 'b': 2} == dict2, 'dict sorted 1 error'

    dict1 = {'b': 2, 'a': 1, 'c': 1}
    dict2 = dict(sorted(dict1.items(), key=itemgetter(1, 0)))
    assert {'a': 1, 'c': 1, 'b': 2}


def test_4():
    list1 = [[1,2,3], \
             [1,3,2], \
             [2,1,3], \
             [2,3,1], \
             [3,1,2], \
             [3,1,1], \
             [3,2,1]]
    # 先按第1列排序,然后是第2列,然后是第3列... 其他的同理, 请自行测试
    list2 = sorted(list1, key=itemgetter(0, 1, 2))
    assert [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 1], [3, 1, 2],
            [3, 2, 1]] == list2, 'sort error'
    
    
def test_5():

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
    assert [{'name': 'a', 'age': 18}, {'name': 'b', 'age': 20}, {'name': 'b', 'age': 19}] == list2, 'list sort key方法错误'
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
    
def test_6():

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
    list2.sort(key=itemgetter('name'))
    assert [{'name': 'a', 'age': 18}, {'name': 'b', 'age': 20}, {'name': 'b', 'age': 19}] == list2, 'list sort key方法错误'
    list2.sort(key=itemgetter('age'))
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
    list2.sort(key=itemgetter('name','age'))
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
