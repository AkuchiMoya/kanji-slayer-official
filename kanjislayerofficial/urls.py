from django.contrib import admin
from django.urls import path, include

from quizgame.views import home_page, player_list_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizgame.urls', namespace="quizgame"))
]
