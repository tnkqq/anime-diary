from aiogram import Bot, Dispatcher,types   
from config import Config
from services.api import AnimeApi
from keyboards import inline_kb
from handlers import text
import logging
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage


#logs
logging.basicConfig(level=logging.INFO)

#bot object
bot = Bot(token = Config.BOT_TOKEN)

storage = MemoryStorage()

#dispatcher object
dp = Dispatcher (bot = bot,storage=storage)


async def main():
    try:
        from handlers import dp
        await bot.delete_webhook(drop_pending_updates=True)
        @dp.message_handler(commands=("start"))
        async def cmd_strt(message : types.Message):    
            await bot.delete_message(message_id= message.message_id,chat_id=message.chat.id)
            image = types.InputFile.from_url(text.hello_img)
            await bot.send_photo(message.chat.id,photo=image,caption=(text.start) ,reply_markup=inline_kb.menu_button) 
        import handlers.message_handlers
        import handlers.cllb_handlers
        await dp.start_polling(bot)
        await dp.skip_updates()
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


