"""
This file contains all the handlers for the bot.
"""
from aiogram import Router, types
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    """
    Handler for the /start command
    """
    await message.answer("Hello! I'm a bot!")
