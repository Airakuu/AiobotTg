from aiogram import F,Router # F для проверки типа сообщения, Router для создания роутера
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove # импортируем типы сообщений и клавиатур
from aiogram.filters.command import Command, CommandStart # импорт фильтров для команд
from aiogram.fsm.context import FSMContext # импорт для работы с состояниями
import keyboard as kb
from states import Reg

user = Router()

@user.message(CommandStart()) # обработчик для команды /start, который запускает регистрацию пользователя
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Привет, рад что ты со мной!\n\nВведите ваше имя:', 
                         reply_markup=ReplyKeyboardRemove())
    await state.set_state(Reg.name)
    
@user.message(Reg.name) # обработчик для состояния Reg.name, который сохраняет имя пользователя и переходит к следующему состоянию
async def reg_name(message: Message, state: FSMContext):
    await state.update_data(name = message.text)
    await message.answer('Теперь отправьте ваш номер телефона!', reply_markup=kb.get_number)
    await state.set_state(Reg.phone)

@user.message(Reg.phone, F.contact) # обработчик для состояния Reg.phone, который сохраняет номер телефона пользователя и завершает регистрацию
async def reg_contact(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    
    data = await state.get_data() 
    await message.answer(f'Вы успешно зарегестировались!\n\n Ваше имя: {data["name"]}\n Ваш номер телефона: {data["phone"]}', reply_markup=kb.menu)
    await state.clear()
    
@user.message(Reg.phone) # обработчик для состояния Reg.phone, который проверяет, что пользователь отправил не контакт, а текст, и просит его отправить номер телефона по кнопке
async def reg_phone(message: Message):
    await message.answer('Отправьте номер телефона по кнопке ниже') # Сука, ебучие состояния, минус час жизни

    
@user.message(F.text == 'Каталог') # обработчик для текстового сообщения "Каталог", который отправляет пользователю сообщение с выбором разделов каталога
async def cmd_catalog(message: Message):
    await message.answer('Выберите раздел каталога', reply_markup=kb.catalog)
    
@user.message(F.text == 'Секрет') # обработчик для текстового сообщения "Секрет", который отправляет пользователю секретное сообщение
async def cmd_secret(message: Message):
    await message.answer('Здравствуй, я бот на aiogram 3.0!')

@user.callback_query(F.data.startswith('brand_')) # обработчик для коллбеков, которые начинаются с "brand_", который извлекает название бренда из callback_data и отправляет пользователю сообщение с выбранным брендом
async def cmd_brand(callback: CallbackQuery):
    brand = callback.data.split('_')[1]
    await callback.answer(None)
    await callback.message.answer(f'Вы выбрали бренд {brand.capitalize()}')

@user.message() # обработчик для всех остальных сообщений, который просто повторяет сообщение пользователя (для проверки работы бота)
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)