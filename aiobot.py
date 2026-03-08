from aiogram import Bot, Dispatcher # импорт для создания бота и диспетчера, Bot для создания экземпляра бота, Dispatcher для обработки сообщений
from aiogram.types import Message
from handlers import user
from config import TOKEN

async def main():
    bot = Bot(token=TOKEN) #импорт токена из config.py, чтобы не светить его в открытом коде(config.py добавлен в .gitignore)
    dp = Dispatcher()
    dp.include_router(user)
    await dp.start_polling(bot) # запуск бота, который будет обрабатывать сообщения и коллбеки, используя диспетчер
    
    
if __name__ == "__main__": # чтобы бот работал
    try:
        import asyncio
        asyncio.run(main())
    except (KeyboardInterrupt):
        pass