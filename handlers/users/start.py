from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.million import million_buttons
from keyboards.default.bravo import bravo_buttons
from keyboards.default.dizayin import dizayin_buttons

from loader import dp,bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum siz bu yerda                                                                                          MILLION DIZAYIN BRAVO KONSERTLARINI topishingiz mumukin👇",reply_markup=menu_buttons)


@dp.message_handler(text='Million konserti')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang👇",reply_markup=million_buttons)


@dp.message_handler(text='Bravo konserti')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang👇",reply_markup=bravo_buttons)


@dp.message_handler(text='Dizayin konserti')
async def bot_start(message: types.Message):
    await message.answer(f"Tanlang👇",reply_markup=dizayin_buttons)



