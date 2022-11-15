from django.shortcuts import render
from django.http import HttpResponse
from .models import Player


def home_page(request):
    return render(request, "home_page.html")

def player_list_page(request):
    players = Player.objects.all()
    context = {
        "players": players
    }

    return render(request, "player_list.html", context)