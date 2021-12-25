# python-2021

## 简介
- python发明者 范罗苏姆，荷兰， 1989年
- 解释型：代码在执行是一行一行的翻译成机器语言
- 优势：可扩展、可嵌入
- 应用领域：人工智能、web爬虫、图形识别

## 代码

### 数据类型
```
一切皆对象：整形也是对象
6种数据类型：
不可变：数字、字符串、元组、frozenset
可变：列表、集合、字典
数字类型：int、bool、float、complex
```
### 转义
```
反斜杠\转义，r让反斜杠不转义
name =r'刘德\n华'  #输出：刘德\n华
```

### 多行语句
- 字符串用\分割，[],{},()不需要用\
```
total = "1" +\
        "2" +\
        "3"
print(total)
total_list = ["1",
              "2",
              "3"]
print(total_list)
```

### 截取
- 前闭后开，最后一个参数为步长，-1表示最末尾的索引
```
print(str[1:5:2])          # 结果为24，输出从第二个开始到第五个且每隔一个的字符（步长为2）

list = ['1','2','3','4','5']
print(list[1:5:2])         # 结果为['2', '4']

```

### 打印
- 打印之后不换行
```

print('name',end='')
print('1234',end='')
```

### 不变性
- 为了防止经常使用的数据频繁的创建或销毁
```
整型 -5~256
字符串

>>> a =1111
>>> b=1111
>>> print(id(a)==id(b))
False

```

### 类型判断
- type不会认为子类是父类，isinstance会认为是
```

# bool是int的子类
is_goods = True
print(isinstance(is_goods,int))         #True
print(type(is_goods)==int)              #False
print(issubclass(type(is_goods),int))   #True

```

### 运算
- // 返回一个整数，或者是浮点数（小数位是0）
- ** 表示乘方
```
>>> print(8/7)
1.1428571428571428
>>> print(8//7)
1
>>> print(2**5)
32

```

### 序列
- str list tuple set map range 都是序列
- set map不支持索引、切片、相加

### 数据转换
```


```

### list
```
# 增删改查，增和删
# 方法：list(p), + , in,
# append 和 extend
# list.index(obj),sort
# 浅复制 和 深度复制
```

### dict
```
# 增删改查
# in, enumerate
# setdefault,update,get,pop,popitem
# sort
# 浅复制 和 深度复制
# 方法：dict(p)
```

