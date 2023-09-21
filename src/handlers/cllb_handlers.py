from . import dp,bot
from aiogram import types
from keyboards import inline_kb
from .message_handlers import UserStates
from aiogram.dispatcher import FSMContext   
from aiogram.dispatcher.filters.state import StatesGroup,State
# from ..keyboards import inline_kb


#menu 
@dp.callback_query_handler(text = "menu_button")
async def push_menu(callback_query:types.CallbackQuery):
    await bot.edit_message_caption(caption="Select action",chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id,reply_markup=inline_kb.menu_select)

#anime search     
@dp.callback_query_handler(text = "search")
async def push_menu(callback_query:types.CallbackQuery, state : FSMContext):
    #!state waiting for anime title...
    await state.set_state(UserStates.WaitigForSearch)
    await bot.edit_message_caption(caption="Input Anime Title :",chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id)
    await state.update_data(MESSAGE_TO_EDIT = callback_query.message.message_id)
    print("leave from clbck")
#my libs     
@dp.callback_query_handler(text = "libs")
async def push_menu(callback:types.CallbackQuery):
    await callback.message.answer(text="Select collection",reply_markup=inline_kb.libs_button)


