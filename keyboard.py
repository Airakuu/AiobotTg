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
        [InlineKeyboardButton(text='Nike', callback_data='brand_nike')],
        [InlineKeyboardButton(text='Adidas', callback_data='brand_adidas')],
        [InlineKeyboardButton(text='Reebok', callback_data='brand_reebok')]
    ]
)