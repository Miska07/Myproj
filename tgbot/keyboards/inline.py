from aiogram import types
import requests
import json

# r_all = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i=52772')
#
# r = requests.get("https://www.themealdb.com/api/json/v1/1/list.php?c=list")
# data = json.loads(r.text)
# # data["Beef"]
# # data["Breakfast"]
# # data["Chicken"]
# # data["Dessert"]
# # data[""]
# #
# #
#
#
#
#
#








kbd = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text=f"сам сайт рецептів", url="https://patelnya.com.ua")],
    [types.InlineKeyboardButton(text=f"Головне меню", callback_data="menu")],
    [types.InlineKeyboardButton(text=(f"КАТЕГОРІЯ"), callback_data="categories")]
])

kdb = types.InlineKeyboardMarkup(inline_keyboard=[
    [types.InlineKeyboardButton(text=f"Beef", callback_data="category_Beef")],
    [types.InlineKeyboardButton(text=f"Breakfast", callback_data="category_Breakfast")],
    [types.InlineKeyboardButton(text=f"Chicken", callback_data="category_Chicken")],
    [types.InlineKeyboardButton(text=f"Dessert", callback_data="category_Dessert")],
    [types.InlineKeyboardButton(text=f"Goat", callback_data="category_Goat")],
    [types.InlineKeyboardButton(text=f"Lamb", callback_data="category_Lamb")],
    [types.InlineKeyboardButton(text=f"Miscellaneous", callback_data="category_Miscellaneous")],
    [types.InlineKeyboardButton(text=f"Pasta", callback_data="category_Pasta")],
    [types.InlineKeyboardButton(text=f"Pork", callback_data="category_Pork")],
    [types.InlineKeyboardButton(text=f"Side", callback_data="category_Side")],
    [types.InlineKeyboardButton(text=f"Starter", callback_data="category_Starter")],
    [types.InlineKeyboardButton(text=f"Vegan", callback_data="category_Vegan")],
    [types.InlineKeyboardButton(text=f"Vegetarian", callback_data="category_Vegeterian")]
])
