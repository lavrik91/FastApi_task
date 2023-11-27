import asyncio
import time

import aiohttp
from ping3 import ping


# task 1
# async def aprint(value=1):
#     print(f'{value} start print')
#     await asyncio.sleep(7)
#     print(f'{value}  end print')
#
#
# async def aprint2(value=2):
#     print(f'{value} start print')
#     await asyncio.sleep(3)
#     print(f'{value}  end print')
#
#
# # task 2
# async def aprint3(value=3):
#     print(f'{value} start print')
#     await asyncio.sleep(5)
#     print(f'{value}  end print')
#
#
# async def main():
#     # coros = [aprint(i) for i in range(3)]
#
#     await asyncio.gather(aprint(), aprint2(), aprint3())
#
#
# asyncio.run(main())


# task 3
# async def url_ping(session, url):
#     try:
#         async with session.get(url) as response:
#             ping_time = ping(url.replace('https://', ''))
#             print(f'{url}  : ping({ping_time:.4f})  :  status({response.status})')
#     except aiohttp.ClientError as e:
#         print(e)
#
#
# async def main():
#     urls = [
#         'https://www.google.com',
#         'https://www.facebook.com',
#         'https://www.youtube.com',
#         'https://www.twitter.com',
#         'https://www.instagram.com',
#         'https://www.linkedin.com',
#         'https://www.reddit.com',
#         'https://www.amazon.com',
#         'https://www.githubb.com'
#     ]
#
#     async with aiohttp.ClientSession() as session:
#         async_tasks = [url_ping(session, url) for url in urls]
#         await asyncio.gather(*async_tasks)
#
#
# asyncio.run(main())


# task 4
# def func():
#     value = 'hi' * (yield)
#     print(value)
#
#
# async def main():
#     f = func()
#     next(f)
#     f.send(3)
#
#
# asyncio.run(main())
