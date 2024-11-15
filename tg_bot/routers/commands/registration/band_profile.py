import json
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from tg_bot.keyboards.kb import ButtonText, get_skip_kb, get_on_start_kb
from tg_bot.request_client.client import Client
from .fsm_form import FormBand

router = Router()

@router.message(Command("group_profile"))
async def create_profile_band(message: Message, state: FSMContext):
    await state.set_state(FormBand.name)
    await message.answer("Как называется ваша группа?",
                         reply_markup=ReplyKeyboardRemove())


@router.message(FormBand.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FormBand.musical_genre)
    await message.answer("В каком стиле играет ваша группа?")


@router.message(FormBand.musical_genre)
async def add_genre(message: Message, state: FSMContext):
    await state.update_data(musical_genre=message.text)
    await state.set_state(FormBand.who_need)
    await message.answer("Кто вам нужен?")


@router.message(FormBand.who_need)
async def add_who(message: Message, state: FSMContext):
    await state.update_data(who_need=message.text)
    await state.set_state(FormBand.info)
    await message.answer("Расскажите немного о своей группе.\n"
                         "Например: сколько ей лет.\n"
                         "Или нажми на кнопку 'Пропустить'⬇️",
                         reply_markup=get_skip_kb())


@router.message(FormBand.info, F.text)
async def add_info(message: Message, state: FSMContext):
    if message.text == ButtonText.SKIP:
        await state.update_data(info="")
    else:
        await state.update_data(info=message.text)
    await state.set_state(FormBand.sample)
    await message.answer(
        text="Отправь небольшой аудио сэмпл своей игры.\n"
             "Или нажми на кнопку 'Пропустить'⬇️",
        reply_markup=get_skip_kb()
    )


@router.message(FormBand.info)
async def handle_invalid_info(message: Message):
    await message.answer("Прости. Но тут надо ввести только текст.\n"
                         "Заполни инфо еще раз.\n"
                         "Или нажми на кнопку 'Пропустить'⬇️",
                         reply_markup=get_skip_kb())


@router.message(FormBand.sample, F.audio)
async def add_sample(message: Message, state: FSMContext):
    audio_id = message.audio.file_id
    data = await state.update_data(sample=audio_id)
    await state.clear()
    user_tg = message.from_user.id
    data.setdefault("user_tg", user_tg)
    client = Client()
    json_data = json.dumps(data, ensure_ascii=False)
    response_text = client.add_band(json_data)
    await message.answer(
        text=f'{response_text}\n'
             f'Теперь вы можете начать искать музыканта😉\n'
             f'Удачи! Жмите на кнопку внизу ⬇️',
        reply_markup=get_on_start_kb()
    )


@router.message(FormBand.sample, F.text == ButtonText.SKIP)
async def add_sample(message: Message, state: FSMContext):
    data = await state.update_data(sample="")
    await state.clear()
    user_tg = message.from_user.id
    data.setdefault("user_tg", user_tg)
    client = Client()
    json_data = json.dumps(data, ensure_ascii=False)
    response_text = client.add_band(json_data)
    await message.answer(
        text=f'{response_text}\n'
             f'Теперь вы можете начать искать музыканта😉\n'
             f'Удачи! Жмите на кнопку внизу ⬇️',
        reply_markup=get_on_start_kb()
    )


@router.message(FormBand.sample)
async def handle_invalid_sample(message: Message):
    await message.answer(
        text="Можно отправить только аудио файл.\n"
             "Попробуй отправить еще раз.\n"
             "Или нажми на кнопку 'Пропустить'⬇️",
        reply_markup=get_skip_kb()
    )
