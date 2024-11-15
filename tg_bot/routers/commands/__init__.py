__all__ = ("router",)

from aiogram import Router
from .base import router as base_commands_router
from .registration import router as registration_router
from .user import router as user_commands_router

router = Router()

router.include_routers(
    base_commands_router,
    user_commands_router,
    registration_router
)