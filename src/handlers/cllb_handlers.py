from bot import dp, bot
from aiogram import types
from keyboards import inline_kb
# from ..keyboards import inline_kb


#menu 
@dp.callback_query_handler(text = "menu_button")
async def push_menu(callback:types.CallbackQuery):
    await callback.message.answer(text="Select action",reply_markup=inline_kb.menu_select)

#anime search     
@dp.callback_query_handler(text = "search")
async def push_menu(callback:types.CallbackQuery):
    await callback.message.answer(text="Input Anime Title :")

#my libs     
@dp.callback_query_handler(text = "libs")
async def push_menu(callback:types.CallbackQuery):
    await callback.message.answer(text="Select collection",reply_markup=inline_kb.libs_button)


