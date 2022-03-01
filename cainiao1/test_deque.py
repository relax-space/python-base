from collections import deque
from itertools import islice


def test_1():
    list = ['a', 'b', 'c']
    d = deque(list)
    assert 'a' == d[0] and 'b' == d[1] and 'c' == d[2], 'queue error'


def test_2():
    data = islice(['a', 'b', 'c'],None)
    d = deque(data)
    assert 'a' == d[0] and 'b' == d[1] and 'c' == d[2], 'queue error'
    
