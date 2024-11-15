import os


class Settings:
    URL_API = "http://127.0.0.1:8000/api/"
    MUSICIAN = 'musician/'
    BAND = 'band/'
    PROFILE = 'profile/'
    TG_MUSICIAN = 'musicians/tg_users/'
    TG_BAND = 'bands/tg_users/'
    TOKEN = os.getenv("BOT_TOKEN")