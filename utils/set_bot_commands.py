from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Run bot"),
            types.BotCommand("help", "Output the help"),
            types.BotCommand("audio", "Download video from YouTube and transfer it to audio")
        ]
    )
