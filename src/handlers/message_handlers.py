import asyncio
from bot import dp, bot
from services.api import AnimeApi
from aiogram import types
from aiogram.types import Message 
from aiogram.dispatcher.filters import Text 

def create_message(anime_data):
    msg = f"🔸Title : {anime_data['russian']} \n" 
    msg += f"🌟 Score : {anime_data['score']} \n" 
    msg += f"🔹Status : {anime_data['status']} \n" 
    msg += f"🔹episodes : {anime_data['episodes']} \n" 
    msg += f"🔹Realese : {anime_data['releasedOn']['year']} \n" 
    msg += f"{anime_data['poster']['originalUrl']} \n" 


    return msg

@dp.message_handler()
async def anime_by_title(message :types.Message):
    anime_title = message.text

    anime_api = AnimeApi(f"{anime_title}")
    anime_data = await anime_api.fetch_anime_data()
    msg=create_message(anime_data)
    # Запускаем асинхронную функцию
    await message.answer (text=msg)




