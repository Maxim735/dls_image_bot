from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
import keyboards as kb
import text_messages as ms


# Хэндлер обрабатывающий нажатие кнопки "главное меню"
@dp.callback_query_handler(text='menu', state='*')
async def transfer_style(call: types.CallbackQuery, state: FSMContext):
    await state.reset_state()
    await call.message.answer(ms.menu_message, parse_mode='Markdown', reply_markup=kb.start_keyboard())
    await call.answer()
