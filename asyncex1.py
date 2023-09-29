import asyncio


async def task1():
    print('1st email')
    asyncio.create_task(task2())
    await asyncio.sleep(2)
    print('1st sent')


async def task2():
    print('2nd email')
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print('2nd sent')


async def task3():
    print('3rd email')
    await asyncio.sleep(2)
    print('3rd sent')


asyncio.run(task1())