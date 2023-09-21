from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup 

menu_button = [[InlineKeyboardButton(text = "Menu", callback_data="menu_button"),]]

menu_select = [[InlineKeyboardButton(text = "Anime Search",callback_data="search"),
                InlineKeyboardButton(text = "My Lib's ",callback_data="libs")]]

libs_button = [[InlineKeyboardButton(text = 'Viewed',callback_data='viewed'),
                InlineKeyboardButton(text = 'To view',callback_data='to_view')]]


anime_button = [InlineKeyboardButton(text = 'Rate',callback_data = 'rate'),
                InlineKeyboardButton(text = 'To bookmarks',callback_data='anime_to_bookmarks'),
                InlineKeyboardButton(text = "Anime Search",callback_data="search"),
                InlineKeyboardButton(text = "My Lib's ",callback_data="libs")]

menu_select = InlineKeyboardMarkup(inline_keyboard=menu_select)
menu_button = InlineKeyboardMarkup(inline_keyboard=menu_button)
libs_button = InlineKeyboardMarkup(inline_keyboard=libs_button)
anm_func_button = InlineKeyboardMarkup(row_width=2)
anm_func_button.add(*anime_button)

