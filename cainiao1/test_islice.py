
from itertools import islice


def test_1():
    data = 'abcdef'
    # 从索引0开始,从索引2(因为不包括3,所以是2)结束, 最后一个参数2 是步长,每次2个
    res = islice(data, 0, 3, 2)
    assert res.__next__() == 'a' and res.__next__() == 'c', 'islice error'
