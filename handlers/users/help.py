from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("List of commands ",
            "1. select the button from the menu /audio",
            "2. paste the link of any youtube video from which you want to extract the audio track",
            "3. Wait a minute and enjoy the music")

    await message.answer("\n".join(text))

