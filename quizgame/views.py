from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from .models import Player, HiraganaAnswer
from .forms import HiraganaQuestionModelForm, HiraganaAnswerModelForm, PlayerModelForm

# CRUD - Create, Retreive, Update, Delete + List

class LandingPageView(TemplateView):
    template_name = "landing.html"


class HiraganaAnswerListView(ListView):
    template_name = "hiragana_list.html"
    queryset = HiraganaAnswer.objects.all()
    context_object_name = "hiragana"


class HiraganaQuestionCreateView(CreateView):
    template_name = "hiragana_create_question.html"
    form_class = HiraganaQuestionModelForm
    
    def get_success_url(self):
        return reverse("quizgame:home-page")


class HiraganaAnswerCreateView(CreateView):
    template_name = "hiragana_create_answer.html"
    form_class = HiraganaAnswerModelForm

    def get_success_url(self):
        return reverse("quizgame:home-page")


class HiraganaAnswerDeleteView(DeleteView):
    template_name = "hiragana_delete_answer.html"
    queryset = HiraganaAnswer.objects.all()

    def get_success_url(self):
        return reverse("quizgame:home-page")


def hiragana_delete(request, pk):
    hiragana_to_delete = HiraganaAnswer.objects.get(hiragana_question_id=pk)
    hiragana_to_delete.delete()
    return redirect("/hiragana")


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