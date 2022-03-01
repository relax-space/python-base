# 1.格式化的方式
# 2.填充零的方式
# 3.常用方法[编码,查找并替换,strip,split,isdecimal,isspace]
import re

# pytest -vs cainiao1/test_str.py


def test_1():
    # 1.格式化的方式
    dog = 'dog'
    str1 = 'This is a %s' % dog
    str2 = 'This is {} {}'.format('a', dog)
    str3 = f'This is a {dog}'
    assert 'This is a dog' == str1, r'% format error'
    assert 'This is a dog' == str2, '{} format error'
    assert 'This is a dog' == str3, 'f-string format errorr'


def test_2():
    # 2.填充零的方式
    price = 123
    str1 = '%04d' % price
    str2 = str(price).rjust(4, '0')
    str3 = str(price).zfill(4)
    assert '0123' == str1, '% format error'
    assert '0123' == str2, 'rjust error'
    assert '0123' == str3, 'zfill error'


def test_3():
    # 3 编码
    c = '中国'
    b1 = c.encode('utf-8')
    assert b'\xe4\xb8\xad\xe5\x9b\xbd' == b1, 'encode error'
    str1 = b1.decode('utf-8')
    assert '中国' == str1, 'decode error'


def test_4():
    # 4 startswith,find
    raw = 'hello world $1 $2'
    b1 = raw.startswith('hello')
    assert b1, 'startswith error'
    i1 = raw.find('$')
    i2 = raw.rfind('$')
    assert 12 == i1, 'find error'
    assert 15 == i2, 'rfind error'


def test_5():
    # 查找并替换
    raw = 'hello world hello 1'
    str1 = raw.replace('hello', 'good', 1)
    assert 'good world hello 1' == str1, 'replace error'

    reg = re.compile(r'^hello')
    str2 = reg.sub('good', raw)
    assert 'good world hello 1' == str2, 'replace error'

    reg = re.compile(r'hello')
    str3 = reg.sub('good', raw, 1)
    assert 'good world hello 1' == str3, 'replace error'


def test_6():
    # strip
    raw = 'madam'
    str1 = raw.strip('am')
    assert 'd' == str1, 'strip error'


def test_7():
    # split
    raw = 'I am  from jingzhou'
    a1 = raw.split(' ')
    assert {'I', 'am', 'from', '', 'jingzhou'} == set(a1), 'split error'
    # \s+ 正则表示用1个或者多个空格分割,所以am  from之间的两个空格会当做1个分割符去分割
    a2 = re.split(r'\s+', raw)
    assert {'I', 'am', 'from', 'jingzhou'} == set(a2), 'split re error'


def test_8():
    # 数字 isdecimal 不可以汉字,isdigit 不可以汉字, isnumeric可以汉字
    # 我会优先用isdecimal,因为比较干净
    raw1 = '123'
    raw2 = '五'
    assert raw1.isdecimal() == raw1.isdigit(
    ) == raw1.isnumeric() == True, 'isdecimal error'

    assert not raw2.isdecimal(), 'isdecimal error'
    assert not raw2.isdigit(), 'isdigit error'
    assert raw2.isnumeric(), 'isnumeric error'


def test_9():
    # isspace
    raw = '  '
    assert raw.isspace(), 'isspace error'


def test_10():
    # join
    raw1 = ['a', 'b', 'c']
    assert 'a:b:c' == ':'.join(raw1)
