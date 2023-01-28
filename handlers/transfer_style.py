from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
import keyboards as kb
from states.base import BotStates


# Хэндлер, обрабатывающий нажатие кнопки переноса стиля
@dp.callback_query_handler(text='button_style', state='*')
async def transfer_style(call: types.CallbackQuery, state: FSMContext):
    await BotStates.style.set()
    await call.message.answer('Мне нужно 2 фотографии. Первым делом отправь фотографию стиля.\n'
                              'Если хочешь выбрать из доступных вариантов - нажми на кнопку ниже \U0001F447',
                              reply_markup=kb.style_images())
    await call.answer()

