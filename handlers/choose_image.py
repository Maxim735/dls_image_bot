from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext
import keyboards as kb
from states.base import BotStates
import loader as loader


# Хэндлер, обрабатывающий нажатие кнопки выбора картинки для стиля
@dp.callback_query_handler(text='style_images', state=BotStates.style)
async def transfer_style(call: types.CallbackQuery, state: FSMContext):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()
    for i, image in enumerate(loader.style_images):
        if i == 0:
            media.attach_photo(types.InputFile(image), f"Есть следующие стили:\n\n{loader.styles_text}")
        else:
            media.attach_photo(types.InputFile(image))

    await call.message.answer_media_group(media)
    await call.message.answer("Выбери стиль кнопкой, если ни один не нравится - отправляй собственную"
                              " картинку для стиля\n"
                              "Если ты используешь декстопную версию Telegram, то не забудь поставить галочку\n"
                              f"☑ `Compress images`", parse_mode='Markdown', reply_markup=kb.select_style())
    await call.answer()
