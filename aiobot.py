from aiogram import Bot, Dispatcher
from aiogram.types import Message
from handlers import user

async def main():
    bot = Bot(token='8629283156:AAFQBK42zJC6x1uFmDL6fJHNS4vKcFj-YPE')
    dp = Dispatcher()
    dp.include_router(user)
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except (KeyboardInterrupt):
        pass