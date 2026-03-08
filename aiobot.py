from aiogram import Bot, Dispatcher
from aiogram.types import Message
from handlers import user
from config import TOKEN

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(user)
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except (KeyboardInterrupt):
        pass