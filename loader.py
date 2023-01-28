import os
from dotenv import load_dotenv, find_dotenv
from aiogram import Dispatcher, Bot
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import glob

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')

loop = asyncio.get_event_loop()

bot = Bot(token=BOT_TOKEN, loop=loop)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Загружаем в переменную описание стилей
with open('images/styles/description.txt', encoding='UTF-8') as f:
    styles_text = f.read()

# Пишем в переменную изображения загруженных стилей
style_images = sorted([file for file in glob.glob('images/styles/*.jpg')])
