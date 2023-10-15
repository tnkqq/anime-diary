from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup 

menu_button = [[InlineKeyboardButton(text = "Menu", callback_data="menu_button"),]]

menu_select = [[InlineKeyboardButton(text = "Anime Search",callback_data="search"),]]
                # InlineKeyboardButton(text = "My Lib's ",callback_data="libs")]]

libs_button = [[InlineKeyboardButton(text = 'Viewed',callback_data='viewed'),
                InlineKeyboardButton(text = 'To view',callback_data='to_view')]]


anime_button = [[InlineKeyboardButton(text = 'Rate',callback_data = 'rate'),
                InlineKeyboardButton(text = 'To bookmarks',callback_data='anime_to_bookmarks'),
                InlineKeyboardButton(text = "Anime Search",callback_data="search")]]
                # InlineKeyboardButton(text = "My Lib's ",callback_data="libs")]]
rate_button = [[InlineKeyboardButton(text='1️⃣',callback_data='rate-1')],
               [InlineKeyboardButton(text='2️⃣',callback_data='rate-2')],
               [InlineKeyboardButton(text='3️⃣',callback_data='rate-3')],
               [InlineKeyboardButton(text='4️⃣',callback_data='rate-4')],
               [InlineKeyboardButton(text='5️⃣',callback_data='rate-5')],
               [InlineKeyboardButton(text='6️⃣',callback_data='rate-6')],
               [InlineKeyboardButton(text='7️⃣',callback_data='rate-7')],
               [InlineKeyboardButton(text='8️⃣',callback_data='rate-8')],
               [InlineKeyboardButton(text='9️⃣',callback_data='rate-9')],
               [InlineKeyboardButton(text='🔟',callback_data='rate-10')]]
menu_rate = InlineKeyboardMarkup(inline_keyboard=rate_button)
menu_select = InlineKeyboardMarkup(inline_keyboard=menu_select)
menu_button = InlineKeyboardMarkup(inline_keyboard=menu_button)
menu_libs = InlineKeyboardMarkup(inline_keyboard=libs_button)
anm_func_button = InlineKeyboardMarkup(row_width=2,inline_keyboard=anime_button)

