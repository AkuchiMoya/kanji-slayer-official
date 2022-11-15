from django.urls import path
from .views import home_page, player_list_page

app_name = "quizgame"

urlpatterns = [
    path('', home_page),
    path('players', player_list_page),
]
