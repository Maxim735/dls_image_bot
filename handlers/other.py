from aiogram import types
from loader import dp
from talk_model.model import pipe
import keyboards as kb


# Handler для обработки тех сообщений, что не попадают в остальные
@dp.message_handler(state='*')
async def bot_echo(message: types.Message):
    bot_ans = pipe.predict([message.text])
    await message.answer(bot_ans[0])
