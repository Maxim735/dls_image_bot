from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
from states.base import BotStates
from loader import style_images


# Хэндлер, обрабатывающий нажатие кнопок выбора стиля
@dp.callback_query_handler(lambda call: call.data.startswith('style_'), state=BotStates.style)
async def transfer_style(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['style_img'] = style_images[int(call.data[-1]) - 1]
    await BotStates.content.set()
    await call.message.answer(f"Ты выбрал {int(call.data[-1])} стиль"
                              "\nТеперь отправь мне картинку, на которую нужно перенести стиль\n"
                              "Если ты используешь декстопную версию Telegram, то не забудь поставить галочку\n"
                              f"☑ `Compress images`", parse_mode='Markdown')
    await call.answer()
