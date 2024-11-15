from django.urls import path, include

from .views import hello_world_view, MusicianViewSet, ListTgUsersView, BandViewSet, ListTgBandsView, AllProfileView
from rest_framework.routers import DefaultRouter

app_name = "my_app"

routers = DefaultRouter()
routers.register('musician', MusicianViewSet)
routers.register('band', BandViewSet)

urlpatterns = [
    path('hello/', hello_world_view, name='hello'),
    path('', include(routers.urls)),
    path('musicians/tg_users/', ListTgUsersView.as_view(), name='tg_users'),
    path('bands/tg_users/', ListTgBandsView.as_view(), name='band_tg_users'),
    path('profile/<int:user_tg>', AllProfileView.as_view(), name='profile_tg_user'),
]
