import asyncio
from aiogram import Dispatcher
from . import bot,storage
import traceback
from services.api import AnimeApi
from aiogram import types
from aiogram.types import Message 
from aiogram.dispatcher import FSMContext 
from aiogram.dispatcher.filters import Text 
from aiogram.dispatcher.filters.state import StatesGroup,State

from keyboards import inline_kb 

dp_msg = Dispatcher(bot = bot,storage=storage)


class UserStates(StatesGroup):
    WaitigForSearch = State()

def create_message(anime_data):
    msg = f"🔸Title : {anime_data['russian']} \n" 
    msg += f"🌟 Score : {anime_data['score']} \n" 
    msg += f"🔹Status : {anime_data['status']}  \n" 
    msg += f"🔹episodes : {anime_data['episodes']} \n" 
    msg += f"🔹Realese : {anime_data['releasedOn']['year']} \n" 
    poster = f"{anime_data['poster']['originalUrl']}" 

    return msg,poster


@dp_msg.message_handler(state = UserStates.WaitigForSearch)
async def anime_by_title(message :types.Message, state : FSMContext):
    print("in message")
    anime_title = message.text
    await bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
    anime_api = AnimeApi(f"{anime_title}")
    anime_data = await anime_api.fetch_anime_data()
    msg, poster = create_message(anime_data)
    
    
    message_id_to_edit = (await state.get_data())['MESSAGE_TO_EDIT']
    await bot.edit_message_media(chat_id=message.chat.id, 
                                 message_id=message_id_to_edit,
                                 media=types.InputMediaPhoto(media = poster,caption= msg ),
                                 reply_markup=inline_kb.anm_func_button)
    
    await state.finish()

# @dp.message_handler(state=UserStates.WaitingForRate)
# async def rate_anime(message : types.Message,state : FSMContext):
#     await bot.delete_message(chat_id=message.chat.id,message_id=message.message_id)
#     message_id_to_edit = (await state.get_data())['MESSAGE_TO_EDIT']
#     await bot.edit_message_caption(chat_id=message.chat.id,message_id=message_id_to_edit)