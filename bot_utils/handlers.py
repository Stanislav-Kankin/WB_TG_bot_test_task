from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import aiohttp

import bot_utils.bot_kb as kb
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f'Привет, {message.from_user.first_name}!\n'
        'Если нужна подробная помощь - жми /help',
        reply_markup=kb.main_kb
        )


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(
        'Тут текст по основным командам бота'
    )


@router.message()
async def handle_article(message: Message):
    if message.text == 'Получить информацию по товару':
        await message.answer('Введите артикул товара')
    else:
        user_article = message.text
        url = f'https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={user_article}'

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                result = await response.json()

        if 'error' in result:
            await message.reply('Произошла ошибка при получении информации о товаре.')
            return

        products = result['data']['products']
        if products:
            product = products[0]
            product_info = f"Название: {product['name']}\nБренд: {product['brand']}\nЦена: {product['salePriceU']}\nРейтинг: {float(product['supplierRating'])}"
            await message.reply(product_info, reply_markup=kb.inline)
        else:
            await message.reply('Товар не найден.')
