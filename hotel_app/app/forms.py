# hotel_app/forms.py

from django import forms
from .models import Anketa, Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'agree_to_news']
       
       
       
class AnketaForm(forms.ModelForm):
    CHOICES = [
        ('M', "мужской"),
        ('F', 'женский'),
        # ('unknown', 'unknown'),
    ]
    gender = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
    )

    INTERNET_CHOICES = [
        ('daily', 'Ежедневно'),
        ('every_two_days', 'раз в несколько дней'),
        ('weekly', 'раз в неделю'),
        ('unknown', 'не знаю'),
    ]
    internet = forms.ChoiceField(
        widget=forms.Select,
        choices=INTERNET_CHOICES,
    )

    class Meta:
        model = Anketa
        fields = ['name', 'city', 'job', 'gender', 'internet', 'email', 'message', 'agree_to_news']
