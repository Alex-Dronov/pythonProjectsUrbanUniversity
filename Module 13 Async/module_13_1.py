import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    i = 1
    while i <= 5:
        await asyncio.sleep(10/power)
        print(f'Силач {name} поднял шар номер {i}')
        i += 1
    print(f'Силач {name} закончил соревнования')
    pass

async def start_tournament():
    tsk_pasha = asyncio.create_task(start_strongman('Pasha', 3))
    tsk_denis = asyncio.create_task(start_strongman('Denis', 4))
    tsk_apollon = asyncio.create_task(start_strongman('Apollon', 5))

    await tsk_pasha
    await tsk_denis
    await tsk_apollon

asyncio.run(start_tournament())
