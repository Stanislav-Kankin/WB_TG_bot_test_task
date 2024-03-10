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

inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Перейти на товар.", url='https://www.wildberries.ru/catalog/54997699/detail.aspx')]
        ]
)
