from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Player, HiraganaAnswer
from .forms import HiraganaQuestionModelForm, HiraganaAnswerModelForm, PlayerModelForm, CustomUserCreationForm

# CRUD - Create, Retreive, Update, Delete + List

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return reverse("login")


class LandingPageView(TemplateView):
    template_name = "landing.html"


class HiraganaAnswerListView(LoginRequiredMixin, ListView):
    template_name = "hiragana_list.html"
    queryset = HiraganaAnswer.objects.all()
    context_object_name = "hiragana"


class HiraganaQuestionCreateView(LoginRequiredMixin, CreateView):
    template_name = "hiragana_create_question.html"
    form_class = HiraganaQuestionModelForm
    
    def get_success_url(self):
        return reverse("quizgame:home-page")


class HiraganaAnswerCreateView(LoginRequiredMixin, CreateView):
    template_name = "hiragana_create_answer.html"
    form_class = HiraganaAnswerModelForm

    def get_success_url(self):
        return reverse("quizgame:home-page")


class HiraganaAnswerDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "hiragana_delete_answer.html"
    queryset = HiraganaAnswer.objects.all()

    def get_success_url(self):
        return reverse("quizgame:home-page")


class PlayerListView(LoginRequiredMixin, ListView):
    template_name = "player_list.html"
    queryset = Player.objects.all()
    context_object_name = "players"


class PlayerDetailView(LoginRequiredMixin, DetailView):
    template_name = "player_profile_page.html"
    queryset = Player.objects.all()
    context_object_name = "player"


class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "player_profile_admin_update.html"
    queryset = Player.objects.all()
    form_class = PlayerModelForm

    def get_success_url(self):
        return reverse("quizgame:player-list-page")

    def form_valid(self, form):
        send_mail(
            subject="A player has been updated.",
            message="Visit the website to see who was updated.",
            from_email="test@test.com",
            recipient_list=["test2@test.com"],
        )
        return super(PlayerUpdateView, self).form_valid(form)


