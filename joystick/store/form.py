from django import forms
from django.contrib.auth import get_user_model
from .models import Review


User = get_user_model


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text', 'score',)
        labels = {
            'text': 'Текст отзыва',
            'score': 'Оценка',
        }
        help_texts = {
            'text': 'Текст отзыва (* обязательное поле для заполнения)',
            'score': 'Оценка (* обязательное поле для заполнения)',
        }