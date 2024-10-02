import re


def test_split():
    data1 = "you     are \
        the best"

    res_list = re.split(r"\s+", data1)
    assert ["you", "are", "the", "best"] == res_list, "re split error"


def test_sub():
    data1 = "my mobile is 15811112222"
    num = re.sub(r"^.*is ", "", data1)
    assert "15811112222" == num, "re sub 1 error"

    num = re.sub(r"\D+", "", data1)
    assert "15811112222" == num, "re sub 2 error"

    # 如果分组, 在组外面的is 也是包含在内的
    num = re.sub(r"(.*?)is ", "", data1)
    assert "15811112222" == num, "re sub 3 error"

    # 保留分组, nice, \g<1>表示第一组,如果有多个组,还可以\g<2>
    num = re.sub(r".*?(\d+)", r"\g<1>", data1)
    assert "15811112222" == num, "re sub 4 err"


def test_sub2():
    data1 = "a:1,b:2,c:3"

    def multi(matched):
        v = int(matched.group())
        return str(v * 2)

    res = re.sub(r"\d+", multi, data1)
    assert "a:2,b:4,c:6" == res, "re sub 4 error"


# .*?  .*  .?的区别
def test_x1():
    data1 = "abc12d56dx"
    assert ["12"] == re.findall(r"c(.*?)d", data1), ".*? error"
    assert ["12d56"] == re.findall(r"c(.*)d", data1), ".* error"
    # 没有匹配到，因为没有要求cd直接只能有一个字符或者0个字符，如果想要匹配到，可以修改数据为 data1 = "abc1d2d56dx"
    assert [] == re.findall(r"c(.?)d", data1), ".? error"
