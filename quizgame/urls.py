from django.urls import path
from .views import home_page, player_list_page, player_profile_page, hiragana_list_page

app_name = "quizgame"

urlpatterns = [
    path('', home_page),
    path('players/', player_list_page),
    path('players/<pk>/', player_profile_page),
    path('hiragana/', hiragana_list_page),
]
