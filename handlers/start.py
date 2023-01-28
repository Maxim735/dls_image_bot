from aiogram import types
from loader import dp
import logging
import time
import text_messages as ms
import keyboards as kb
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start'], state="*")
async def start_msg(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id
    user_name = msg.from_user.first_name
    user_full_name = msg.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')

    await msg.reply(f"Привет, {user_full_name} \n {ms.start_message}", parse_mode='Markdown',
                     reply_markup=kb.start_keyboard())
