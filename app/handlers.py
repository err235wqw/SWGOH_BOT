from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.states as st

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await message.answer('Бот как бот, что бубнить то', reply_markup=None)
