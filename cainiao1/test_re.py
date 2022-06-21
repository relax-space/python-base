'''

. \w \s \d a|b () [...] {} * + 

1. 常用元字符

.   匹配除换行符以外的任意字符
\w  匹配字母或数字或下划线
\s  匹配任意的空白符
\d  匹配数字
\n  匹配一个换行符
\t  匹配一个制表符

^   匹配字符串的开始
$   匹配字符串的结尾

\W  匹配非字母或数字或下划线
\D  匹配非数字
\S  匹配非空白符
a|b 匹配字符a或字符b
()  匹配括号内的表达式，也表示一个组
[...]   匹配字符组中的字符
[^...]  匹配除了字符组中字符的所有字符


2. 量词：控制前面的元字符出现的次数


*       重复零次或更多次
+       重复一次或更多次
？      重复零次或一次
{n}     重复n次
{n，}   重复n次货更多次

3. 贪婪匹配和惰性匹配

.*  贪婪匹配
.*? 非贪婪匹配

'''
import re


def test_dot():
    data1 = 'hello \n world'
    pattern = re.compile(r'.+')
    res_list = pattern.findall(data1)
    assert ['hello ', ' world'] == res_list, 're dot error'


def test_dot2():
    # 有时候需要 . 能匹配所有字符,包括换行符, 就需要带上参数 re.S
    data1 = '<input name="hello \n world">'

    # (.+) 括号说明: 正常会取整个<input name="(.+)">,加括号之后,就只取括号里面的了
    ptn = re.compile(r'<input name="(.+)">', re.S)
    res_list = ptn.findall(data1)
    assert ['hello \n world'] == res_list, 're dot 2 error'


def test_w():
    data1 = 'ab_@.121'
    # + 表示重复一次或者更多次,就是说如果条件一直符合的话,就联系输出,比如:ab_
    ptn = re.compile(r'\w+')
    res_list = ptn.findall(data1)
    assert ['ab_', '121'] == res_list, 're w error'


def test_s():
    data1 = 'a b\tc\n d$#'
    ptn = re.compile(r'\s+')
    res_list = ptn.findall(data1)
    assert [' ', '\t', '\n '] == res_list, 're s error'


def test_d():
    data1 = 'yidong 10086,liantong 10010'
    ptn = re.compile(r'\d+')
    res_list = ptn.findall(data1)
    assert ['10086', '10010'] == res_list, 're d error'


def test_start():
    data1 = 'ab1ab2'
    ptn = re.compile(r'ab\d')
    res_list = ptn.findall(data1)
    assert ['ab1', 'ab2'] == res_list, 're ^ error'

    # ^ 表示只匹配字符串的开始
    data1 = 'ab1ab2'
    ptn = re.compile(r'^ab\d')
    res_list = ptn.findall(data1)
    assert ['ab1'] == res_list, 're ^ 2 error'


def test_end():
    data1 = '1ab2ab'
    ptn = re.compile(r'\dab$')
    res_list = ptn.findall(data1)
    assert ['2ab'] == res_list, 're $ error'


def test_and():
    data1 = '12a_3$dc'
    ptn = re.compile(r'\d+|a|d|c')
    res_list = ptn.findall(data1)
    assert ['12', 'a', '3', 'd', 'c'] == res_list, 're | error'


def test_bracket():
    data1 = '<input id="1" name="xiaoxinmiao"/>'
    ptn = re.compile(r'<input id="(\d+)" name="(.+)"/>')
    res_list = ptn.findall(data1)
    assert ('1', 'xiaoxinmiao') == res_list[0], 're () error'


def test_bracket2():
    # 可以设置分组名
    data1 = '<input id="1" name="xiaoxinmiao"/>'
    ptn = re.compile(r'<input id="(?P<id>.*?)" name="(?P<name>.*?)"/>')
    iter_obj = ptn.finditer(data1)
    res_obj = iter_obj.__next__()
    assert '1' == res_obj.group('id') and 'xiaoxinmiao' == res_obj.group(
        'name'), 're () error'


def test_bracket3():
    # 可以设置分组名
    data1 = '<input class="c1" id="1" name="miao1"/><input class="c2" id="2" name="miao2"/>'
    ptn = re.compile(
        r'<input class=".*?" id="(?P<id>.*?)" name="(?P<name>.*?)"/>')
    iter_obj = ptn.finditer(data1)
    ids, names = [], []
    for i in iter_obj:
        ids.append(i.group('id'))
        names.append(i.group('name'))
    assert ['1', '2'] == ids and ['miao1', 'miao2'] == names, 're () error'


def test_bracket_mid():
    data1 = '12dss#$$fwe564_'
    ptn = re.compile(r'[1-9a-z_$]+')
    res_list = ptn.findall(data1)
    assert ['12dss', '$$fwe564_'] == res_list, 're [] error'


def test_bracket_mid2():
    data1 = '12dss#$$fwe564_'
    # [^] 表示不匹配里面的任何数
    ptn = re.compile(r'[^1-9a-z_$]+')
    res_list = ptn.findall(data1)
    assert ['#'] == res_list, 're [] error'

# 这个例子只是为了便于理解,平时并不常用, 常用的是 .*?
def test_liangci():
    data1 = 'abccd'
    # +: 前一个字符出现1次或者多次
    re_list = re.findall(r'abc+', data1)
    assert ['abcc'] == re_list, 're + error'

    # *: 前一个字符出现0次或者多次
    re_list = re.findall(r'abf*', data1)
    assert ['ab'] == re_list, 're + error'

    # ?: 前一个字符出现0次或者1次
    re_list = re.findall(r'abc?', data1)
    assert ['abc'] == re_list, 're + error'


def test_star():
    data1 = '<input id="" name=""/>'
    # 这不是我们期待的结果
    res_list = re.findall(r'<input id="(.+?)" name="(.+?)"/>', data1, re.S)
    assert [] == res_list, 're + error'

    # 这是我们期待的结果,做了两个分组,就应该返回两组数据
    res_list = re.findall(r'<input id="(.*?)" name="(.*?)"/>', data1, re.S)
    assert ('', '') == res_list[0], 're + error'


def test_star2():
    # .* 贪婪
    data1 = '我爱北京天安门,天安门上太阳升.'
    res_list = re.findall(r'我爱(.*)天安门', data1)
    assert ['北京天安门,'] == res_list, 're .* error'
    # .*? 非贪婪
    res_list = re.findall(r'我爱(.*?)天安门', data1)
    assert ['北京'] == res_list, 're .* error'


def test_bracket_big():
    # 只有两位数字才符合要求
    data1 = 'a1b12c134d1234e'
    res_list = re.findall(r'\d{2}', data1)
    assert ['12', '13', '12', '34'] == res_list, r're {} error'
    # 两位,以及两位以上的数字都符合要求
    data1 = 'a1b12c134d1234e'
    res_list = re.findall(r'\d{2,}', data1)
    assert ['12', '134', '1234'] == res_list, r're {} error'


def test_zh():
    data1 = '我爱111北京%天安🍬___%$|&门'
    res_list = re.findall(r'[\u4e00-\u9fa5]+', data1)
    assert '我爱北京天安门' == ''.join(res_list), r're zh error'
