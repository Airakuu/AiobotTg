from aiogram import F,Router
from aiogram.types import Message
from aiogram.filters.command import Command, CommandStart 

user = Router()
@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, рад что ты со мной!')

@user.message(F.text == 'Привет')
async def cmd_hello(message: Message):
    await message.answer('Здравствуй, я бот на aiogram 3.0!')

@user.message(F.photo)
async def cmd_photo(message: Message):
    await message.answer('Ты отправил фото, его id: ' + message.photo[-1].file_id)
    await message.answer_photo(message.photo[-2].file_id)
  
@user.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Ты нажал помощь!')

@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)