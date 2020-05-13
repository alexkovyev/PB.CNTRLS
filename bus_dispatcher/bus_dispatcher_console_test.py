import asyncio
import random


class Disp:
    """
    Bus dispatcher class. Immitates message sending and result checking by
    randomly choosing either command is executed or not.
    """
    def __init__(self, loop):
        self.loop = loop
        self.commands = asyncio.Queue()
        self.loop.create_task(self.__executor())

    async def start_command(self, future, command):
        await self.commands.put((command, future))

    async def __executor(self):
        """
        Endless task that sends messages from queue
        """
        while True:
            command, future = await self.commands.get()
            await asyncio.sleep(5)# constraints output frequency
            result = random.randrange(0, 20)# choosing randomly if task is executed or not
            if 'initiate' in command:
                print(command.split()[1], 'initiated')
                future.set_result('initiated')
            elif result == 0:
                print('dispatcher:', command, 'done')
                future.set_result('done')
            else:
                print('dispatcher:', command, 'not ready')
                future.set_result('not ready')


class Unit:
    """
    Base class for all units. Realizes common unit behavior, such as
    executing commands (check controller's status until command is done)
    """
    def __init__(self, disp: Disp, address):
        self.disp = disp
        self.address = address

    async def execute_command(self, command):
        future = self.disp.loop.create_future()
        await self.disp.start_command(future, 'initiate ' + command)
        await future
        while future.result() != 'done':
            print('unit:', command, 'ready?')
            future = self.disp.loop.create_future()
            await self.disp.start_command(future, command)
            await future


class CutTable(Unit):
    def __init__(self, disp: Disp, address):
        super().__init__(disp, address)

    async def cut(self):
        await self.execute_command('cut')
        print('CutTable: cut has been done!')


class Oven(Unit):
    def __init__(self, disp: Disp, address):
        super().__init__(disp, address)

    async def give(self):
        await self.execute_command('bake')
        print('Oven: bake has been done!')


loop = asyncio.get_event_loop()
disp = Disp(loop=loop)
cut_table = CutTable(disp, 0)
oven = Oven(disp, 0)


async def pbm():
    await asyncio.gather(
        cut_table.cut(),
        oven.give()
    )


async def main():
    _pbm = loop.create_task(pbm())
    await _pbm


if __name__ == "__main__":
    loop.run_until_complete(main())
