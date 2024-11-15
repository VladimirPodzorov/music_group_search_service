__all__ = ("router",)

from aiogram import Router
from .user_handlers import router as user_router
from .user_commands import router as user_commands_router
from .handler_callback_query import router as callback_router

router = Router()

router.include_routers(
    user_router,
    user_commands_router,
    callback_router,
)
