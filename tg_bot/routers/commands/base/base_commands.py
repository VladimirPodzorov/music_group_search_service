from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tg_bot.keyboards.kb import get_on_start_kb

router = Router(name=__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    print("IDDDDDD=",message.from_user.id)
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Кого ты ищешь?", reply_markup=get_on_start_kb())


