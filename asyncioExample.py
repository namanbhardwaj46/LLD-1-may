

import asyncio

def greet(name):
    print(f"Hello, {name}!")

async def printHello():
    greet("World")
    await asyncio.sleep(1)
    print("hello world 2")


async  def awaits():
    await asyncio.sleep(2)
    await printHello()

if __name__ == '__main__':
    greet("abc")
    asyncio.run(printHello())

    greet("def")
    asyncio.run(awaits())


