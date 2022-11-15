from django.contrib import admin

from .models import User, Player, HiraganaQuestion, HiraganaAnswer

admin.site.register(User)
admin.site.register(Player)
admin.site.register(HiraganaQuestion)
admin.site.register(HiraganaAnswer)