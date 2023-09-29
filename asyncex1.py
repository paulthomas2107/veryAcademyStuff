import asyncio


async def task1():
    print('1st email')
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print('1st sent')


async def send_mail():
    print('Test')
    await asyncio.sleep(2)
    print('Awake')


async def task2():
    print('2nd email')
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print('2nd sent')


async def task3():
    print('3rd email')
    await asyncio.sleep(1)
    print('3rd sent')
    print("End")


async def t1():
    await t2()
    print('t1')


async def t2():
    await t3()
    print('t2')


async def t3():
    print('t3')


# print(asyncio.iscoroutinefunction(test1()))
asyncio.run(send_mail())
asyncio.run(t1())
