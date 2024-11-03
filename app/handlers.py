from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

import app.keyboards as kb
import app.states as st

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(st.menu.start_page)
    await message.answer('Это бот гильдии Dominance Of The Sith, входящей в состав альянса BT. Выберите ', reply_markup=kb.main)

@router.message(st.menu.start_page, F.text == 'Территориальные битвы')
async def TB_menu(message: Message, state: FSMContext):
    await state.set_state(st.menu.TB)
    await message.answer('Выберите необходимую вам информацию', reply_markup=kb.TB)
