from aiogram import F,Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command, CommandStart
import keyboard as kb

user = Router()
@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, рад что ты со мной!', reply_markup=kb.menu)

@user.message(F.text == 'Каталог')
async def cmd_hello(message: Message):
    await message.answer('Выберите раздел каталога', reply_markup=kb.catalog)
    
@user.message(F.text == 'Секрет')
async def cmd_hello(message: Message):
    await message.answer('Здравствуй, я бот на aiogram 3.0!')

@user.callback_query(F.data.startswith('brand_'))
async def cmd_brand(callback: CallbackQuery):
    brand = callback.data.split('_')[1]
    await callback.message.answer(f'Вы выбрали бренд {brand.capitalize()}')

@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)