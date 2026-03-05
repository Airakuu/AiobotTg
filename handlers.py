from aiogram import F,Router
from aiogram.types import Message
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

@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)