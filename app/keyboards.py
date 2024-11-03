from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Территориальные битвы'), KeyboardButton(text='Войны Гильдий')],
                                     [KeyboardButton(text='Нажал - стал офицером по таблицам'), KeyboardButton(text='На ягер главе')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню')
TB = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Общий план ТБ'), KeyboardButton(text='План на этап')],
                                   [KeyboardButton(text='Список персоонажей для взводов'), KeyboardButton(text='Предыдущий результат ТБ')]],
                         resize_keyboard=True,
                         input_field_placeholder='Выберите нужную информацию')
