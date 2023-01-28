from aiogram.dispatcher.filters.state import State, StatesGroup


class BotStates(StatesGroup):
    '''
    Класс: машина состояний бота
    style: состояние обработки фото стиля
    content: состояние обработки фото контента
    upgrade: состояние улучшения качества фото
    talk: состояние болтовни
    '''
    style = State()
    content = State()
    upgrade = State()
    talk = State()
