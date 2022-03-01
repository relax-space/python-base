'''
说明: 生成器可以用next迭代 或调用send方法,send不仅可以获取迭代数据,还可以发送参数
'''

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         break

while True:
    try:
        print(f.send(None),end=' ')
    except StopIteration:
        break
