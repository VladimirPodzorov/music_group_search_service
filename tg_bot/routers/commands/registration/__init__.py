__all__ = ("router",)

from aiogram import Router
from .profile import router as profile_router
from .band_profile import router as band_profile_router

router = Router()
router.include_routers(
    profile_router,
    band_profile_router,
)
