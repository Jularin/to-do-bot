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


if __name__ == '__main__':
    executor.start_polling(dp)
