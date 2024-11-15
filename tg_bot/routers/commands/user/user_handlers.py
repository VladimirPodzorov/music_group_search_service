from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils import markdown

from tg_bot.keyboards.inline_kb import build_action_kb
from tg_bot.keyboards.kb import ButtonText, get_create_musician_kb, get_create_band_kb
from tg_bot.request_client.client import Client

router = Router()

band_list_pk = []
musician_list_pk = []

def user_exist(user_id):
    client = Client()
    user_ids = client.get_musicians_tg_id()
    return user_id in user_ids


def band_exist(user_id):
    client = Client()
    user_ids = client.get_bands_tg_id()
    return user_id in user_ids


def pre_request(pk_lst, user_tg):
    lst = [i['pk'] for i in pk_lst if i['user_tg'] != user_tg]
    return lst


@router.message(F.text == ButtonText.MUSICIAN)
async def get_musician(message: Message):
    client = Client()
    global musician_list_pk
    user = message.from_user.id
    if band_exist(user):
        if not musician_list_pk:
            musician_list_pk = pre_request(client.list_musician(), user)
        resp = client.get_musician_response(str(musician_list_pk[0]))
        message_text = markdown.text(
            markdown.hbold(f'Имя: {resp["name"].title()}'),
            markdown.hbold(f'Возраст: {resp["age"]}'),
            markdown.hbold(f'Инструмент: {resp["musical_instrument"].title()}'),
            markdown.hbold(f'Опыт игры: {resp["experience"]}'),
            markdown.hbold(f'Доп. инфо: {resp["info"]}'),
            sep="\n"
        )
        if resp["avatar"]:
            await message.answer_photo(
                photo=resp["avatar"],
                caption=message_text,
                parse_mode=ParseMode.HTML,
                reply_markup=build_action_kb(resp["user_tg"]),
            )
        else:
            await message.answer(message_text, reply_markup=build_action_kb(resp["user_tg"]), parse_mode=ParseMode.HTML)

        if resp["sample"]:
            await message.answer_audio(audio=resp["sample"], caption="Сэмпл")

        del musician_list_pk[0]
    else:
        await message.answer(
            text="Создайте анкету группы, чтобы начать поиск музыканта.\n"
                 "Жми на кнопку внизу ⬇️",
            reply_markup=get_create_band_kb()
        )

@router.message(F.text == ButtonText.BAND)
async def get_band(message: Message):
    client = Client()
    global band_list_pk
    user = message.from_user.id
    if user_exist(user):
        if not band_list_pk:
            band_list_pk = pre_request(client.list_band(), user)

        resp = client.get_bands_response(str(band_list_pk[0]))
        message_text = markdown.text(
            markdown.hbold(f'Имя: {resp["name"].title()}'),
            markdown.hbold(f'Жанр: {resp["musical_genre"]}'),
            markdown.hbold(f'Нужен: {resp["who_need"].title()}'),
            markdown.hbold(f'Доп. инфо: {resp["info"]}'),
            sep="\n"
        )
        if resp["sample"]:
            await message.answer_audio(
                audio=resp["sample"],
                caption=message_text,
                reply_markup=build_action_kb(resp["user_tg"]),
                parse_mode=ParseMode.HTML
            )
        else:
            await message.answer(message_text, reply_markup=build_action_kb(resp["user_tg"]))

        del band_list_pk[0]
    else:
        await message.answer(
            text="Создайте анкету музыканта, чтобы начать поиск группы.\n"
                 "Жми на кнопку внизу ⬇️",
            reply_markup=get_create_musician_kb()
        )
