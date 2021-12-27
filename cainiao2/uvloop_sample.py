'''
uvloop: uvloop可以提升协程的效率
'''
import asyncio
import platform


async def req1():
    return 1

if platform.system().lower() != 'windows':
    # 在windows系统上会有警告,不过可以正常运行,因为windows不走这段代码
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
print(asyncio.run(req1()))
