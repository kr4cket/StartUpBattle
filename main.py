from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor

TOKEN_API = '6523870902:AAF9DvID8t_SCbdpZU0spg4QIaf4xeW4ZQM'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
