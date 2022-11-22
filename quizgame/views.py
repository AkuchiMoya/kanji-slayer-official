from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, HiraganaAnswer, HiraganaQuestion
from .forms import HiraganaQuestionModelForm, HiraganaAnswerModelForm, PlayerModelForm


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


def player_profile_admin_update(request, pk):
    player = Player.objects.get(id=pk)
    form = PlayerModelForm(instance=player)
    if request.method == "POST":
        form = PlayerModelForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect("/players")
    context = {
        "form": form,
        "player": player,
    }
    return render(request, "player_profile_admin_update.html", context)


def hiragana_list_page(request):
    hiragana = HiraganaAnswer.objects.all()
    context = {
        "hiragana": hiragana
    }
    return render(request, "hiragana_questions.html", context)


def hiragana_create_question(request):
    form = HiraganaQuestionModelForm()
    if request.method == "POST":
        form = HiraganaQuestionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/hiragana")
    context = {
        "form": form
    }
    return render(request, "hiragana_create_question.html", context)


def hiragana_create_answer(request):
    form = HiraganaAnswerModelForm()
    if request.method == "POST":
        form = HiraganaAnswerModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/hiragana")
    context = {
        "form": form
    }
    return render(request, "hiragana_create_answer.html", context)