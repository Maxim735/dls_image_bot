from aiogram import types
from loader import dp
import keyboards as kb


# Хэндлер, обрабатывающий нажатие кнопки "Примеры"
@dp.callback_query_handler(text='examples', state='*')
async def transfer_style(call: types.CallbackQuery):
    await types.ChatActions.upload_photo()
    media = types.MediaGroup()

    media.attach_photo(types.InputFile('./images/examples/example_1.jpg'), 'Деревня Пикассо')
    media.attach_photo(types.InputFile('./images/examples/example_2.jpg'), 'Акварельная сова')
    media.attach_photo(types.InputFile('./images/examples/example_3.jpg'), 'Набросок волка')
    await call.message.answer_media_group(media)

    await call.message.answer('Понравились примеры? Попробуй сам!\n\n'
                              'Жми на кнопку \U0001F447', reply_markup=kb.start_keyboard())
    await call.answer()
