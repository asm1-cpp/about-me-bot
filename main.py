import asyncio
from aiogram import Bot, Dispatcher
import config
from bot.handlers import router
from bot.logging import starting

async def main():
    starting()

    if not config.TOKEN or config.TOKEN == "NULL":
        return

    bot = Bot(token=config.TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass
