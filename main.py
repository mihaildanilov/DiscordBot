from bot import bot
from secrets import token
import asyncio
import nest_asyncio

nest_asyncio.apply()


async def main():
    await bot.load_extension("Dice")
    await bot.run(token)


asyncio.run(main())
