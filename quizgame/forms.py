from django import forms
from .models import HiraganaAnswer, HiraganaQuestion

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


