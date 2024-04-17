

url = "https://v6.exchangerate-api.com/v6/8bd81d61c4929bc64ea55ab1/"



import asyncio
import logging
import sys
from os import getenv

import requests
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold


TOKEN = getenv("6821900581:AAHML5Ekjk9-V-q8BK65LN-NtN3U31tTNl0")

dp = Dispatcher()


@dp.message(CommandStart('start'))
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@dp.message(Command('UZS'))
async def echo_handler(message: types.Message) -> None:
    javob = requests.get(url + f"latest/UZS/")
    sum = javob.json()["conversion_rates"]
    natija = str()
    await message.answer(f"USD: {sum['USD']}\nEURO: {sum['EUR']}")




@dp.message(Command('USD'))
async def echo_handler(message: types.Message) -> None:
    response = requests.get(url + f"latest/USD/")
    currency = response.json()["conversion_rates"]
    result = str()
    for key, value in currency.items():
        result +=f"{key}: {value}\n"
    await message.answer(result)

async def main() -> None:
    bot = Bot("6821900581:AAHML5Ekjk9-V-q8BK65LN-NtN3U31tTNl0", parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


