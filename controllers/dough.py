import asyncio
from controllers.events import cntrls_events
import random


async def give(unit_number):
    await asyncio.sleep(5)
    cntrls_events.hardware_status_changed('owen_cell_2', 'broken')
    await asyncio.sleep(5)

    return random.randrange(0, 2)
