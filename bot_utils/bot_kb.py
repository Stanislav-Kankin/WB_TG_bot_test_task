from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton
    )

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Получить информацию по товару')],
        [KeyboardButton(text='Остановить уведомления'),
         KeyboardButton(text='получить информацию из БД')]
    ],
    resize_keyboard=True
)