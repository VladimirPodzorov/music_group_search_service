import json
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from tg_bot.keyboards.kb import ButtonText, get_skip_kb, get_on_start_kb
from tg_bot.request_client.client import Client
from .fsm_form import FormMusician

router = Router()


@router.message(Command("musician_profile"))
async def create_profile_artist(message: Message, state: FSMContext):
    await state.set_state(FormMusician.name)
    await message.answer("Как тебя зовут?",
                         reply_markup=ReplyKeyboardRemove())

@router.message(FormMusician.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FormMusician.age)
    await message.answer("Сколько тебе полных лет?")

@router.message(FormMusician.age)
async def add_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(FormMusician.musical_instrument)
    await message.answer("На каком инструменте ты играешь?")

@router.message(FormMusician.musical_instrument)
async def add_musical_instrument(message: Message, state: FSMContext):
    await state.update_data(musical_instrument=message.text)
    await state.set_state(FormMusician.experience)
    await message.answer("Как долго ты играешь на, указанном тобой, инструменте?")

@router.message(FormMusician.experience)
async def add_experience(message: Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await state.set_state(FormMusician.info)
    await message.answer(
        text="Можешь добавить доп. информацию о себе.\n"
             "Например: в каком жанре ты играешь.\n"
             "Или нажми на кнопку 'Пропустить'⬇️",
        reply_markup=get_skip_kb()
    )


@router.message(FormMusician.info, F.text)
async def add_info(message: Message, state: FSMContext):
    if message.text == ButtonText.SKIP:
        await state.update_data(info="")
    else:
        await state.update_data(info=message.text)
    await state.set_state(FormMusician.avatar)
    await message.answer(
        text="Отправь свое фото на аватар.\n"
             "Или нажми на кнопку 'Пропустить'⬇️",
        reply_markup=get_skip_kb()
    )

@router.message(FormMusician.info)
async def handle_invalid_info(message: Message):
    await message.answer("Прости. Но тут надо ввести только текст.\n"
                         "Заполни инфо еще раз.\n"
                         "Или нажми на кнопку 'Пропустить'⬇️",
                         reply_markup=get_skip_kb())


@router.message(FormMusician.avatar, F.photo)
async def add_avatar(message: Message, state: FSMContext):
    await state.update_data(avatar=message.photo[-1].file_id)
    await state.set_state(FormMusician.sample)
    await message.answer(
        text="Отправь небольшой аудио сэмпл своей игры.\n"
             "Или нажми на кнопку 'Пропустить'⬇️",
        reply_markup=get_skip_kb()
    )


@router.message(FormMusician.avatar, F.text == ButtonText.SKIP)
async def skip_avatar(message: Message, state: FSMContext):
    await state.update_data(avatar="")
    await state.set_state(FormMusician.sample)
    await message.answer(
        text="Отправь небольшой аудио сэмпл своей игры.\n"
             "Или нажми на кнопку 'Пропустить'⬇️",
        reply_markup=get_skip_kb()
    )

@router.message(FormMusician.avatar)
async def handle_invalid_avatar(message: Message):
    await message.answer(
        text="Можно отправить только фото.\n"
             "Попробуй отправить еще раз.\n"
             "Или нажми на кнопку 'Пропустить'⬇️",
        reply_markup=get_skip_kb()
    )


@router.message(FormMusician.sample, F.text == ButtonText.SKIP)
async def add_sample(message: Message, state: FSMContext):
    data = await state.update_data(sample="")
    await state.clear()
    user_tg = message.from_user.id
    data.setdefault("user_tg", user_tg)
    client = Client()
    json_data = json.dumps(data, ensure_ascii=False)
    client.add_musician(json_data)
    await message.answer("Теперь вы можете начать искать группу😉\n"
                             "Ваш профиль будет виден тем, кто ищет участника для группы.\n"
                             "Так вы быстрее найдете себе коллектив."
                             "Удачи! Жмите на кнопку внизу ⬇️",
                             reply_markup=get_on_start_kb())


@router.message(FormMusician.sample, F.audio)
async def add_sample(message: Message, state: FSMContext):
    audio_id = message.audio.file_id
    data = await state.update_data(sample=audio_id)
    await state.clear()
    user_tg = message.from_user.id
    data.setdefault("user_tg", user_tg)
    client = Client()
    json_data = json.dumps(data, ensure_ascii=False)
    client.add_musician(json_data)
    await message.answer("Теперь вы можете начать искать группу😉\n"
                             "Ваш профиль будет виден тем, кто ищет участника для группы.\n"
                             "Так вы быстрее найдете себе коллектив."
                             "Удачи! Жмите на кнопку внизу ⬇️",
                             reply_markup=get_on_start_kb())


@router.message(FormMusician.sample)
async def handle_invalid_sample(message: Message):
    await message.answer(
        text="Можно отправить только аудио файл.\n"
             "Попробуй отправить еще раз.\n"
             "Или нажми на кнопку 'Пропустить'⬇️",
        reply_markup=get_skip_kb()
    )