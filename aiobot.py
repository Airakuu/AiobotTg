from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command, CommandStart 
bot = Bot(token='8629283156:AAFQBK42zJC6x1uFmDL6fJHNS4vKcFj-YPE')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, рад что ты со мной!')
    
@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Ты нажал помощь!')

@dp.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)

'''async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except (KeyboardInterrupt):
        pass'''