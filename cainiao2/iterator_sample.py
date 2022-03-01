'''
说明: 如果是for循环迭代器,则不会抛StopIteration异常
迭代器: 迭代器是一个可以记住遍历的位置的对象。
'''


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 2:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
# 用for从迭代器获取值
for i in myiter:
    print(f'for {i}')

# 用next从迭代器获取值
myiter2 = iter(myclass)
print(f'next {next(myiter2)}')
print(f'next {next(myiter2)}')
print(f'next {next(myiter2)}')
