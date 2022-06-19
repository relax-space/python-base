'''
说明: []的使用
'''


def test_1():
    a = 2
    b = 1
    assert 1 == [a, b][a > b], '[ error'

    c = 3
    assert 2 == [a, c][a > c], '[ error 2'
