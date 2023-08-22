from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup 

menu_button = [[InlineKeyboardButton(text = "Menu", callback_data="menu_button"),]]
menu_select = [
    [InlineKeyboardButton(text = "Anime Search",callback_data="search"),InlineKeyboardButton(text = "My Lib's ",callback_data="libs")]
    ]

libs_button = [[InlineKeyboardButton(text = "Viewed",callback_data="viewed"),InlineKeyboardButton(text = "To view",callback_data="to_view")]]

menu_select = InlineKeyboardMarkup(inline_keyboard=menu_select)
menu_button = InlineKeyboardMarkup(inline_keyboard=menu_button)
libs_button = InlineKeyboardMarkup(inline_keyboard=libs_button)
