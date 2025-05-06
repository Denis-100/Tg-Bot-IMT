import asyncio

from aiogram import Bot, Dispatcher
from handlers import router

token = "8032579193:AAEoc18vvxKsM8O9kxiG9wb70XAsNtwgyL0"


async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)
    await asyncio.gather(
        dp.start_polling(bot)
    )

if __name__ == "__main__":
    try:
        print("Бот включен")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")