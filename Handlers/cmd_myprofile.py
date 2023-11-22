from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command('myprofile'))
async def cmd_myprofile(message: Message):
    await message.answer(
        'chlen'
    )