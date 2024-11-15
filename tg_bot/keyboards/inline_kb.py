from sys import prefix

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


DELETE = "delete"
PATCH = "patch"

class CBData(CallbackData, prefix="data"):
    action: str
    endpoint: str
    pk: int


def build_action_kb(usr_id):
    builder = InlineKeyboardBuilder()
    builder.button(text=f"{'💬Написать'}", url=f'tg://user?id={usr_id}')
    builder.adjust(1)
    return builder.as_markup()


def build_del_patch_kb(endpoint, pk):
    builder = InlineKeyboardBuilder()
    builder.button(text="Редактировать", callback_data=CBData(action=PATCH, endpoint=endpoint, pk=pk))
    builder.button(text="Удалить", callback_data=CBData(action=DELETE, endpoint=endpoint, pk=pk))
    builder.adjust(2)
    return builder.as_markup()
