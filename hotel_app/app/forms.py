# hotel_app/forms.py


from random import choices
from django import forms
from .models import  Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message', 'agree_to_news']
       

class AnketaForm(forms.Form) :
    second_name = forms.CharField(label='Фамилия', min_length=2, max_length=100)
    first_name = forms.CharField(label='Имя', min_length=2, max_length=100)
    reservation = forms.ChoiceField(label='Насколько быстро и просто вы забронировали номер? ',
                                 choices=(('5', '5'),
                                          ('4', '4'),
                                          ('3', '3'),
                                          ('2', '2'),
                                          ('1', '1')), initial=5)  
    city = forms.CharField(label= 'Bаш город', min_length=2, max_length=100)
    job = forms.CharField(label='Ваш род занятий', min_length=2, max_length=100)
    work = forms.ChoiceField(label='Оцените качество работы персонала',
                                choices=[('1','1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                                widget=forms.RadioSelect, initial=5)
    back = forms.ChoiceField(label='Хотели бы вы приехать к нам еще?',
                                choices=[('1','Да'), ('2', 'Нет')],
                                widget=forms.RadioSelect, initial=1)     
    
    email=forms.EmailField(label='Baш e-mail', min_length=7)
    message = forms.CharField(label='Форма отзыва', widget=forms.Textarea(attrs={'rows':5,'cols':25}))
    notice = forms.BooleanField(label='Хочу получать новости на электронную почту', required=False)