'''
多线程例子: 每个请求时间是2秒,并发执行两个请求,最后花费时间小于4秒
'''
import time
from collections import deque
from threading import Thread

import requests

resp_queue = deque()


def req(seconds):
    url = f'https://deelay.me/{seconds*1000}/http://httpbin.org/get?a={seconds}'
    resp = requests.get(url)
    resp_queue.append(resp)


t1 = time.time()
tasks = [Thread(target=req, args=(i,)) for i in [2, 2]]

for i in tasks:
    i.start()

for i in tasks:
    i.join()

for i in resp_queue:
    print(i.json()['args']['a'])

print(f'耗时:{round(time.time()-t1,1)}')


'''
输出:
    2
    2
    耗时:3.1
'''