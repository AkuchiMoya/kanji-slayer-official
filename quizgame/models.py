from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_content_contributor = models.BooleanField(default=False)
    level = models.IntegerField(default=1)
    xp = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class HiraganaQuestion(models.Model):
    question_text = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.question_text


class HiraganaAnswer(models.Model):
    hiragana_question = models.OneToOneField(HiraganaQuestion, on_delete=models.CASCADE, primary_key=True)
    answer_text = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.answer_text


def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created == True:
        UserProfile.objects.create(user=instance)
        Player.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)