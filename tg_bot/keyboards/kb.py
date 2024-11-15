from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

class ButtonText:
    MUSICIAN = "музыкант"
    BAND = "группа"
    SKIP = "Пропустить"
    MUSICIAN_PROFILE = "/musician_profile"
    MUSICIAN_BAND = "/group_profile"


def get_on_start_kb():
    artist = KeyboardButton(text=ButtonText.MUSICIAN)
    band = KeyboardButton(text=ButtonText.BAND)
    buttons = [artist, band]
    markup = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True, one_time_keyboard=False)
    return markup


def get_skip_kb():
    skip = KeyboardButton(text=ButtonText.SKIP)
    buttons = [skip]
    markup = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True, one_time_keyboard=True)
    return markup

def get_create_musician_kb():
    musician = KeyboardButton(text=ButtonText.MUSICIAN_PROFILE)
    buttons = [musician]
    markup = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True, one_time_keyboard=True)
    return markup

def get_create_band_kb():
    band = KeyboardButton(text=ButtonText.MUSICIAN_BAND)
    buttons = [band]
    markup = ReplyKeyboardMarkup(keyboard=[buttons], resize_keyboard=True, one_time_keyboard=True)
    return markup
