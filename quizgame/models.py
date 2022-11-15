from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)


class HiraganaQuestion(models.Model):
    question_text = models.CharField(max_length=20)

    def __str__(self):
        return self.question_text


class HiraganaAnswer(models.Model):
    hiragana_question = models.OneToOneField(HiraganaQuestion, on_delete=models.CASCADE, primary_key=True)
    answer_text = models.CharField(max_length=20)

    def __str__(self):
        return self.answer_text

