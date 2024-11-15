from aiogram.fsm.state import State, StatesGroup

class FormMusician(StatesGroup):
    name = State()
    age = State()
    musical_instrument = State()
    experience = State()
    info = State()
    avatar = State()
    sample = State()

class FormBand(StatesGroup):
    name = State()
    musical_genre = State()
    who_need = State()
    info = State()
    sample = State()