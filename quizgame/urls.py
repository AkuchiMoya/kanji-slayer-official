from django.urls import path
from .views import (
    HiraganaAnswerListView, HiraganaQuestionCreateView, HiraganaAnswerCreateView, HiraganaAnswerDeleteView,
    PlayerListView, PlayerDetailView, PlayerUpdateView
    )

app_name = "quizgame"

urlpatterns = [
    path('', HiraganaAnswerListView.as_view(), name='home-page'),
    path('<int:pk>/delete/', HiraganaAnswerDeleteView.as_view(), name='hiragana-delete'),
    path('createquestion/', HiraganaQuestionCreateView.as_view(), name='hiragana-create-question'),
    path('createanswer/', HiraganaAnswerCreateView.as_view(), name='hiragana-create-answer'),
    path('players/', PlayerListView.as_view(), name='player-list-page'),
    path('players/<int:pk>/', PlayerDetailView.as_view(), name='player-profile-page'),
    path('players/<int:pk>/adminedit/', PlayerUpdateView.as_view(), name='player-profile-admin-update'),
]
