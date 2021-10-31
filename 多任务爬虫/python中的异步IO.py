# 协程原理：yield
import asyncio
#详细见 https://docs.python.org/zh-cn/3/library/asyncio.html?highlight=asyncio
import random


# def fun1():
#     print('---1---')
#     gevent.sleep(2)
#     print('---1---')


async def fun2(n):
    print(f'this is {n},start')
    await asyncio.sleep(random.random() * 3)
    print(f'this is {n},end')


# 创建事件循环
loop = asyncio.get_event_loop()
#  创建生成器列表（任务列表）
tasks = [fun2(i) for i in range(5)]
#  把任务注册到事件循环中，进行执行
loop.run_until_complete(asyncio.wait(tasks))
#  关闭时间循环
loop.close()
