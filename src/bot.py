from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode

from dotenv import dotenv_values
config = dotenv_values(".env")
BOT_TOKEN = config.get("BOT_TOKEN")

from src.logic import form_router

# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML) # type: ignore

"""Start the bot."""

dp = Dispatcher()
dp.include_router(form_router)

