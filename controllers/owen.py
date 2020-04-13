import asyncio


async def bake(cell, recipe):
    """
    Initiate baking in cell by recipe
    :param cell: number of cell
    :param recipe: bake program that cell should follow
    :return: code result
    """
    await asyncio.sleep(90)
    return 1
