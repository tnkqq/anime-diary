from aiogram import Bot, Dispatcher
from config import config
from services.api import AnimeApi

import asyncio
bot = Bot(token = config.token)
dp = Dispatcher (bot = bot)

async def main():
    from handlers import dp
    try:
        await dp.start_polling()

    finally: 
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except(KeyboardInterrupt,SystemExit):
        print("Bot stoped...")





# anime_api = AnimeApi("Bunny girl")

# # Запускаем асинхронную функцию
# import asyncio
# loop = asyncio.get_event_loop()
# loop.run_until_complete(anime_api.fetch_anime_data())