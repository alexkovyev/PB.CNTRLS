import asyncio
from controllers.events import cntrls_events
import random


def foo():
    print("foo")


async def cut(trajectory):
    """
    :param trajectory: trajectory or recipe, will decide later
    :return: result code
    """
    await asyncio.sleep(10)
    cntrls_events.qr_scanned('228337')
    await asyncio.sleep(10)

    return random.randrange(0, 2)


async def move(point):
    """
    Moves basket to the given point. Need for 'rose' slicing.
    :param point: where to move basket
    :return: result code
    """
    await asyncio.sleep(5)
    return 1
