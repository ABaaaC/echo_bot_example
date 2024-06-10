from aiogram.fsm.state import State, StatesGroup

class ConversationStates(StatesGroup):
    ECHO_STATE = State()


import logging
# Enable logging
fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
clrd_fmt = '\x1b[38;5;226m' + fmt + '\x1b[0m'
logging.basicConfig(format=fmt, level=logging.INFO, )
logger = logging.getLogger(__name__)


import os, json

from dotenv import dotenv_values
config = dotenv_values(".env")
BOT_TOKEN = config.get("BOT_TOKEN")
BASE_WEBHOOK_URL = config.get("BASE_WEBHOOK_URL")
WEBHOOK_PATH = config.get("WEBHOOK_PATH")

# bind localhost only to prevent any external access
WEB_SERVER_HOST = config.get("WEB_SERVER_HOST")
# Port for incoming request from reverse proxy. Should be any available port
WEB_SERVER_PORT = config.get("WEB_SERVER_PORT")
#!/usr/bin/env python


import math

from aiogram.enums import ParseMode
from aiogram import types, Router #,F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from aiogram.types.input_file import FSInputFile

from aiohttp import ClientSession, FormData

form_router = Router()


@form_router.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:


    await state.clear()
    

    logger.info("Start is really calling")
    await message.answer(text="Пожалуйста, выберете город:")
    await state.set_state(ConversationStates.ECHO_STATE)

@form_router.message(ConversationStates.ECHO_STATE)
async def start(message: Message, state: FSMContext) -> None:    

    logger.info("echo message")
    text = message.text
    await message.answer(text=text)

