from aiogram import F,Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.command import Command, CommandStart
from aiogram.fsm.context import FSMContext
import keyboard as kb
from states import Reg

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Привет, рад что ты со мной!\n\nВведите ваше имя:', 
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reg.name)
    
@user.message(Reg.name)
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer('Теперь отправьте ваш номер телефона!', reply_markup=kb.get_number)
    await state.set_state(Reg.phone)

@user.message(Reg.phone, F.contact)
async def reg_contact(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    
    data = await state.get_data()
    await message.answer(f'Вы успешно зарегестировались!\n\n Ваше имя: {data["name"]}\n Ваш номер телефона: {data["phone"]}', reply_markup=kb.menu)
    await state.clear()
    
@user.message(Reg.phone)
async def reg_phone(message: Message):
    await message.answer('Отправьте номер телефона по кнопке ниже')

    
@user.message(F.text == 'Каталог')
async def cmd_catalog(message: Message):
    await message.answer('Выберите раздел каталога', reply_markup=kb.catalog)
    
@user.message(F.text == 'Секрет')
async def cmd_secret(message: Message):
    await message.answer('Здравствуй, я бот на aiogram 3.0!')

@user.callback_query(F.data.startswith('brand_'))
async def cmd_brand(callback: CallbackQuery):
    brand = callback.data.split('_')[1]
    await callback.answer(None)
    await callback.message.answer(f'Вы выбрали бренд {brand.capitalize()}')

@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)