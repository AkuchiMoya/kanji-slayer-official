from django.db import models

# Create your models here.
class HiraganaQuestion(models.Model):
    question_text = models.CharField(max_length=20)

    def __str__(self):
        return self.question_text

class HiraganaAnswer(models.Model):
    hiragana_question = models.OneToOneField(HiraganaQuestion, on_delete=models.CASCADE, primary_key=True)
    answer_text = models.CharField(max_length=20)

    def __str__(self):
        return self.answer_text

