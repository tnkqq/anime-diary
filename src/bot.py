from aiogram import Bot, Dispatcher,types   
from config import Config
from services.api import AnimeApi
from keyboards import inline_kb
from handlers import text
import logging
import asyncio
from aiogram.contrib.fsm_storage.redis import RedisStorage2
# from aiogram.contrib.fsm_storage.memory import MemoryStorage

#logs

logging.basicConfig(level=logging.INFO)

#bot object
bot = Bot(token = Config.BOT_TOKEN)

#storages 

# storage = MemoryStorage()

storage = RedisStorage2('localhost', 6379, db=5,pool_size=10,prefix='my_fsm_key')

#dispatcher object
dp= Dispatcher(bot = bot,storage=storage)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    from handlers import dp
    
    async def cmd_strt(message : types.Message): 
        print("cmnd start") 
        await bot.delete_message(message_id= message.message_id, chat_id=message.chat.id)
        image = types.InputFile.from_url(text.hello_img)
        await bot.send_photo(message.chat.id, photo=image, caption=(text.start), reply_markup=inline_kb.menu_button)
    try:
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

