from django.urls import path
from .views import (
    HiraganaAnswerListView, HiraganaQuestionCreateView, HiraganaAnswerCreateView, HiraganaAnswerDeleteView,
    player_list_page, player_profile_page, player_profile_admin_update
    )

app_name = "quizgame"

urlpatterns = [
    path('', HiraganaAnswerListView.as_view(), name='home-page'),
    path('<int:pk>/delete/', HiraganaAnswerDeleteView.as_view(), name='hiragana-delete'),
    path('createquestion/', HiraganaQuestionCreateView.as_view(), name='hiragana-create-question'),
    path('createanswer/', HiraganaAnswerCreateView.as_view(), name='hiragana-create-answer'),
    path('players/', player_list_page, name='player-list-page'),
    path('players/<int:pk>/', player_profile_page, name='player-profile-page'),
    path('players/<int:pk>/adminedit/', player_profile_admin_update, name='player-profile-admin-update'),
]
