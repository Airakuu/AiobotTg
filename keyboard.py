from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог')],
        [KeyboardButton(text='Корзина'),
        KeyboardButton(text='Контакты')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие'
)

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Секрет', url='https://www.youtube.com/watch?v=PYu58TDDkBc')],
        [InlineKeyboardButton(text='Ютуб', url='https://www.youtube.com')],
        [InlineKeyboardButton(text='Гитхаб', url='https://www.github.com')]
    ]
)