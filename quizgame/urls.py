from django.urls import path
from .views import home_page, player_list_page, player_profile_page, hiragana_list_page, hiragana_create_question, hiragana_create_answer, player_profile_admin_update, hiragana_delete

app_name = "quizgame"

urlpatterns = [
    path('', home_page, name='home-page'),
    path('players/', player_list_page, name='player-list-page'),
    path('players/<int:pk>/', player_profile_page, name='player-profile-page'),
    path('players/<int:pk>/adminedit/', player_profile_admin_update, name='player-profile-admin-update'),
    path('hiragana/', hiragana_list_page, name='hiragana-list-page'),
    path('hiragana/createquestion/', hiragana_create_question, name='hiragana-create-question'),
    path('hiragana/createanswer/', hiragana_create_answer, name='hiragana-create-answer'),
    path('hiragana/<int:pk>/delete', hiragana_delete, name='hiragana-delete'),
]
