"""
This module tests controllers api mock's.
It initiates cut and give commands, waits for them and prints if the command was complited or not.
There's two mock events in this commands: qr in cut command and hardware_status in give command.
They arise in the middle of the command execution.
Custom handlers in this modules prints about events.

Expected:
Owen broken event must occur before give command is finished.

QR event must arise before cut command is finished.

Commands results generates randomly, so the can be either executed or not.

"""
from controllers import cut_table
from controllers import dough
from controllers.events import cntrls_events
import asyncio


# Event handlers
def qr_handler(guid):
    print('QR has been scanned. GUID:', guid)


def status_handler(unit_name, status):
    print(unit_name, 'status changed. Now:', status)


# bind handlers to a corresponding event
cntrls_events.bind(qr_scanned=qr_handler)
cntrls_events.bind(hardware_status_changed=status_handler)


# coroutines for controllers' tasks
async def give_dough():
    res = await dough.give('mock')
    if res == 1:
        print('Dough gived')
    else:
        print("Can't give dough")


async def cut_smth():
    res = await cut_table.cut('mock')
    if res == 1:
        print('I have cut them all')
    else:
        print("Mission failed. Returning to HQ")


async def main():
    await asyncio.gather(
        give_dough(),
        cut_smth()
    )


asyncio.run(main())
