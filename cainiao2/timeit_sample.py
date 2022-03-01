from collections import deque
from timeit import timeit

t1 = timeit(setup='a=["A","B","C"]',
            stmt='for i in range(1000000): b=a.pop(0);a.append(b)', number=10, globals=globals())
print(t1)

t2 = timeit(setup='a=deque(["A","B","C"])',
            stmt='for i in range(1000000): a.rotate(-1)', number=10, globals=globals())
print(t2)

# 最快
t3 = timeit(setup='a=deque(["A","B","C"])',
            stmt='for i in range(1000000): b=a.popleft();a.append(b)', number=10, globals=globals())
print(t3)


'''
输出:
    0.1690914
    0.1436717
    0.09824650000000001
'''
