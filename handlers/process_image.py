import asyncio
import os
import threading
from aiogram import Bot
from aiogram import types
from loader import bot, dp, loop
from aiogram.dispatcher import FSMContext
from states.base import BotStates
import logging
import keyboards as kb
from style_model import model
import loader


# Функция вызывающая сам трансфер и отсылающая пользователю результат
# запускаем в потоке через threading.Trhread, так бот не будет зависать во время обработки изображений
# и сможет общаться с другими пользователями.
async def style_transfer(message, style_image, content_image):
    new_image = model.run_nst(style_image, content_image)

    logging.info(f"Finished Style Transfer")

    tmp_bot = Bot(token=os.getenv('BOT_TOKEN'), loop=loader.loop)
    await tmp_bot.send_photo(message.chat.id, photo=new_image)
    await tmp_bot.send_message(message.chat.id, "Готово! \U0001F44D\U0001F44D \n\n"
                                                "Если хочешь попробовать еще, жми \U0001F447\U0001F447",
                               reply_markup=kb.start_keyboard())
    await tmp_bot.close()


async def style_transfer(message, style_image, content_image):
    new_image = model.run_nst(style_image, content_image)

    logging.info(f"Finished Style Transfer")

    tmp_bot = Bot(token=os.getenv('BOT_TOKEN'), loop=loop)
    await tmp_bot.send_photo(message.chat.id, photo=new_image)
    await tmp_bot.send_message(message.chat.id, "Готово! \U0001F44D\U0001F44D \n\n"
                                                "Если хочешь попробовать еще, жми \U0001F447\U0001F447",
                               reply_markup=kb.start_keyboard())
    await tmp_bot.close()


# Хэндлер, обрабатывающий картинку стиля от пользователя
@dp.message_handler(content_types=['photo'], state='*')
async def style_download(msg: types.Message, state: FSMContext):
    current_state = await state.get_state()
    logging.info(current_state)
    logging.info(current_state == 'BotStates:style')
    image = msg.photo[-1]
    img = await bot.download_file_by_id(image.file_id)

    if current_state == 'BotStates:style':
        async with state.proxy() as data:
            data['style_img'] = img
        await BotStates.content.set()
        await msg.answer("Теперь отправь мне картинку, на которую нужно перенести стиль")

    elif current_state == 'BotStates:content':
        async with state.proxy() as data:
            data['content_img'] = img
        data = await state.get_data()
        style_img = data['style_img']
        content_img = data['content_img']
        await state.reset_state()
        await msg.answer("Идёт обработка, это может занять до 5 минут...  \n\U000023F1   \U000023F1   \U0001F51C")
        threading.Thread(
            target=lambda mess, style_img, content_img:
            asyncio.run(style_transfer(mess, style_img, content_img)),
            args=(msg, style_img, content_img)).start()

    else:
        await msg.answer("Прежде чем отправлять мне картинки нажми кнопку\n *Перенести стиль* \U0001F447",
                         parse_mode='Markdown', reply_markup=kb.start_keyboard())
