import asyncio
from aiogram import Dispatcher
from BotToken import bot


async def main():
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    