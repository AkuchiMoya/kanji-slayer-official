from django.shortcuts import render
from django.http import HttpResponse
from .models import Player, HiraganaAnswer


def home_page(request):
    return render(request, "home_page.html")


def player_list_page(request):
    players = Player.objects.all()
    context = {
        "players": players
    }
    return render(request, "player_list.html", context)


def player_profile_page(request, pk):
    player = Player.objects.get(id=pk)
    context = {
        "player": player
    }
    return render(request, "player_profile_page.html", context)


def hiragana_list_page(request):
    hiragana = HiraganaAnswer.objects.all()
    context = {
        "hiragana": hiragana
    }
    return render(request, "hiragana_questions.html", context)