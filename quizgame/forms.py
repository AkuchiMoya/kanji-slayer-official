from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import HiraganaAnswer, HiraganaQuestion, Player

# This was created as part of the site registration implementation so that we can use our own user model. 
User = get_user_model()


class HiraganaQuestionModelForm(forms.ModelForm):
    class Meta:
        model = HiraganaQuestion
        fields = (
            'question_text',
        )


class HiraganaAnswerModelForm(forms.ModelForm):
    class Meta:
        model = HiraganaAnswer
        fields = (
            'hiragana_question',
            'answer_text',
        )


class PlayerModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = (
            'user',
            'level',
            'xp',
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
