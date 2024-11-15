from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils import markdown

from config import Settings
from tg_bot.keyboards.inline_kb import build_del_patch_kb
from tg_bot.request_client.client import Client

router = Router()

@router.message(Command("myprofile"))
async def my_profile_handler(message: Message):
    user_tg = message.from_user.id
    client = Client()
    req = client.get_my_profile(str(user_tg))
    if req["Анкета музыканта"]:
        musician_profile = req["Анкета музыканта"][0]

        message_text_musician = markdown.text(
            markdown.hbold(f'Имя: {musician_profile["name"].title()}'),
            markdown.hbold(f'Возраст: {musician_profile["age"]}'),
            markdown.hbold(f'Инструмент: {musician_profile["musical_instrument"].title()}'),
            markdown.hbold(f'Опыт игры: {musician_profile["experience"]}'),
            markdown.hbold(f'Доп. инфо: {musician_profile["info"]}'),
            sep="\n"
        )
        if musician_profile["avatar"]:
            await message.answer_photo(
                photo=musician_profile["avatar"],
                caption=message_text_musician,
                parse_mode=ParseMode.HTML,
                reply_markup=build_del_patch_kb(endpoint=Settings.BAND, pk=musician_profile["pk"])
            )
        else:
            await message.answer(
                message_text_musician,
                parse_mode=ParseMode.HTML,
                reply_markup=build_del_patch_kb(endpoint=Settings.BAND, pk=musician_profile["pk"])
            )

        if musician_profile["sample"]:
            await message.answer_audio(audio=musician_profile["sample"], caption="Сэмпл")

    if req["Анкета группы"]:
        band_profile = req["Анкета группы"][0]

        message_text_band = markdown.text(
            markdown.hbold(f'Имя: {band_profile["name"].title()}'),
            markdown.hbold(f'Жанр: {band_profile["musical_genre"]}'),
            markdown.hbold(f'Нужен: {band_profile["who_need"].title()}'),
            markdown.hbold(f'Доп. инфо: {band_profile["info"]}'),
            sep="\n"
        )
        if band_profile["sample"]:
            await message.answer_audio(
                audio=band_profile["sample"],
                caption=message_text_band,
                parse_mode=ParseMode.HTML,
                reply_markup=build_del_patch_kb(endpoint=Settings.BAND, pk=band_profile["pk"])
            )
        else:
            await message.answer(
                message_text_band,
                reply_markup=build_del_patch_kb(endpoint=Settings.BAND, pk=band_profile["pk"])
            )
