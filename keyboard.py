from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог')],
        [KeyboardButton(text='Корзина'),
        KeyboardButton(text='Контакты')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие'
) # Главное меню, которое отображается после регистрации пользователя, с кнопками для перехода в каталог, корзину и контакты

catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Секрет?', url='https://www.youtube.com/watch?v=PYu58TDDkBc')],#От гномика
        [InlineKeyboardButton(text='Кнопка для Лёхи', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1')], #Рикролл для Лёхи, он просил
        [InlineKeyboardButton(text='Reebok', callback_data='brand_reebok')]
    ]
) # Клавиатура для каталога, которая отображается при нажатии на кнопку "Каталог", с кнопками для выбора разделов каталога и секретной кнопкой от гномика

get_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Отправить номер', request_contact=True)]
    ],
    resize_keyboard=True
) # Клавиатура для получения номера телефона, которая отображается при запросе номера телефона у пользователя, с кнопкой для отправки контакта