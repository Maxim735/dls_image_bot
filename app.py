import logging
from loader import dp, storage
from aiogram import executor
from commands.default_commands import set_default_commands
import handlers


logging.basicConfig(level=logging.INFO)


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)


async def on_shutdown():
    await storage.close()
    logging.info('Goodbye!')

if __name__ == '__main__':
    executor.start_polling(dp)
