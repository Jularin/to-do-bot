import logging
import asyncio

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor

# initialization
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

loop = asyncio.get_event_loop()


TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    """Handle start command"""
    await bot.send_message(message.from_user.id, "Hi, user!")


@dp.message_handler
async def message_handling(message: types.Message):
    """Echo all messages"""
    await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
