from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

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
async def cms_help(message: Message):
    await message.answer('Тут текст')