import requests
from aiogram import Dispatcher, types

from aiogram.dispatcher.filters import Text, Command, CommandHelp, CommandStart
from tgbot.keyboards.inline import kbd
from tgbot.keyboards.inline import kdb

async def show_category_meals(call:types.CallbackQuery):
    category = call.data.split("_")[1]
    r_category = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}")
    meals = r_category.json()
    meals = meals["meals"]

    kbb = types.InlineKeyboardMarkup()
    for meal in meals:
        #await call.message.answer_photo(photo=meal['strMealThumb'], caption=meal['strMeal'])
        kbb.add(types.InlineKeyboardButton(text=meal['strMeal'], callback_data=f"meal_{meal['idMeal']}"))

    await call.message.answer(text="обери блюдо", reply_markup=kbb)
    await call.answer(text="ns [[etdsq ghtgjl tckb yt gjvjuftim extybrf d d 11 yjxb)")
async def show_meal(call:types.CallbackQuery):
    idMeal = call.data.split("_")[1]
    r_meals = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={idMeal}")
    meal = r_meals.json()
    meal = meal["meals"][0]
    name = meal["strMeal"]
    ins = meal["strInstructions"]
    photo = meal["strMealThumb"]
    youtube = meal["strYoutube"]
    text = f"<b>{name}</b>\n{ins}\n{youtube}"
    if len(text)<=1024:
        await call.message.answer_photo(photo=photo, caption=text, parse_mode="html")

    else:
        await call.message.answer_photo(photo=photo)
        await call.message.answer(text=text, disable_web_page_preview=True)

    await call.answer(text="ns [[etdsq ghtgjl tckb yt gjvjuftim extybrf d d 11 yjxb)", show_alert=True)













async def start(object: types.Message|types.CallbackQuery):
    if type(object)==types.CallbackQuery:
        await object.answer()
        message = object.message
    else:
        message = object
    await message.answer("Привіт я cook.bot і я допоможу тобі знайти рецепт!", reply_markup=kbd)
async def categories(call:types.CallbackQuery):
    await call.message.answer("список категорій", reply_markup=kdb)

def register_user(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'] )
    dp.register_callback_query_handler(start, text="menu")
    dp.register_callback_query_handler(categories, text="categories")
    dp.register_callback_query_handler(show_category_meals, Text(startswith='category_'))
    dp.register_callback_query_handler(show_meal, Text(startswith="meal_"))