import asyncio


def give():
    await asyncio.sleep(3)
    return 1
