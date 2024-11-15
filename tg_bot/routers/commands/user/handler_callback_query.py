from aiogram import Router, F
from aiogram.types import CallbackQuery

from tg_bot.keyboards.inline_kb import DELETE, CBData, PATCH
from tg_bot.request_client.client import Client

router = Router()


@router.callback_query(CBData.filter(F.action == DELETE))
async def delete(callback_query: CallbackQuery, callback_data: CBData):
    await callback_query.answer()
    client = Client()
    endpoint = callback_data.endpoint
    pk = callback_data.pk
    answer = client.delete_profile(endpoint=endpoint, pk=pk)
    await callback_query.message.answer(text=answer)


@router.callback_query(CBData.filter(F.action == PATCH))
async def delete(callback_query: CallbackQuery, callback_data: CBData):
    await callback_query.answer()
    await callback_query.message.answer("in process")
