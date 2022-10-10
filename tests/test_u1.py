from util.u1 import get_dir, to_second


def test_to_second():
    a = to_second('10')
    assert 10 == a, 'to_second error 1'

    a = to_second('10:10')
    assert 610 == a, 'to_second error 2'

    a = to_second('2:10:10')
    assert 7810 == a, 'to_second error 3'


def test_get_dir():
    a = get_dir()
    assert r'D:\1.source\pythonpath\python-base\util' == a, 'get_dir error'
