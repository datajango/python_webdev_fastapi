import asyncio
import time


async def foo(text: str, secs: int):
    await asyncio.sleep(secs)
    # time.sleep(secs)
    print(text)


async def main():
    # await foo('5 secs', 5)
    # await foo('1 secs', 1)
    # await foo('2 secs', 2)
    # await foo('3 secs', 3)
    # await foo('4 secs', 4)
    await asyncio.gather(foo('5 secs', 5), foo('1 secs', 1), foo('2 secs', 2), foo('3 secs', 3), foo('4 secs', 4))


if __name__ == '__main__':
    asyncio.run(main())
