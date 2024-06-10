from aiogram.fsm.state import State, StatesGroup

class ConversationStates(StatesGroup):
    ECHO_STATE = State()


import logging
# Enable logging
fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
clrd_fmt = '\x1b[38;5;226m' + fmt + '\x1b[0m'
logging.basicConfig(format=fmt, level=logging.INFO, )
logger = logging.getLogger(__name__)


from aiogram import Router #,F
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext

from aiogram.types import (
    Message,
)

form_router = Router()

@form_router.message(CommandStart())
async def start(message: Message, state: FSMContext) -> None:


    await state.clear()

    logger.info("Start is really calling")
    await message.answer(text="Режим эхо включен.")
    await state.set_state(ConversationStates.ECHO_STATE)

@form_router.message(ConversationStates.ECHO_STATE)
async def start(message: Message, state: FSMContext) -> None:    

    logger.info("echo message")
    text = message.text
    await message.answer(text=text)

