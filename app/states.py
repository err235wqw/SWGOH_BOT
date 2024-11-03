from aiogram.fsm.state import State, StatesGroup

class menu(StatesGroup):
    start_page = State()
    TB = State()
    GW = State()
    Officer = State()
    Donate = State()