import asyncio


async def set_mode(window, mode):
    """
    Sets mode in window. Mode consists of LED strip light mode and screen content.
    :param window:which window must change it's mode.
    :param mode:state that window should implement (e.g. 'error', 'bon apetti')
    :return: code result
    """
    await asyncio.sleep(1)
    return 1


async def wait_until_dispensed(window):
    """
    Set dispenser window to wait until customer takes his pizza.
    :param window: window number
    :return: code result
    """
    await(asyncio.sleep(60))
    return 1
