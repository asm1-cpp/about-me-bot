from aiogram.fsm.state import StatesGroup, State


class BetterCallAdill(StatesGroup):
    waiting_for_contact = State()
    waiting_for_comment = State()
