import datetime
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render,redirect
from datetime import datetime

from django.contrib.auth.forms import UserCreationForm

from .forms import  FeedbackForm
from .forms import AnketaForm



from django.contrib.auth.forms import UserCreationForm

from django.db import models

from .models import Blog

def blog(request):

    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    assert isinstance(request, HttpRequest)



    return render(

        request,

        'app/blog.html',

        {

            'title':'Блог',

            'posts': posts, # передача списка статей в шаблон веб-страницы

            'year':datetime.now().year,

        }

    )
    
def blogpost(request, parametr):



    assert isinstance(request, HttpRequest)

    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру

    return render(

        request,

        'app/blogpost.html',

        {

            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы

            'year':datetime.now().year,

        }

    )
    

def registration(request):
    if request.method=="POST":
        regform=UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f=regform.save(commit=False)
            reg_f.is_staff=False
            reg_f.is_active=True
            reg_f.is_superuser=False
            reg_f.date_joined=datetime.now()
            reg_f.last_login=datetime.now()
        regform.save()
        
        return redirect('home')
    else:
        regform=UserCreationForm()
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'regform':regform,
            'year':datetime.now().year,
        }
    )
    
def home(request):
    assert isinstance(request,HttpRequest)
    return render(
        request,
        'app/index.html',
       { 'title':'Главная',
        'year': datetime.now().year,}
    )
    

    



from django.shortcuts import render, redirect
from .forms import AnketaForm

def anketa_view(request):
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['second_name'] = form.cleaned_data['second_name']
            data['first_name'] = form.cleaned_data['first_name']
            data['reservation'] = form.cleaned_data['reservation']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['work'] = form.cleaned_data['work']
            data['back'] = form.cleaned_data['back']
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            data['notice'] = form.cleaned_data['notice']
            
            # Сохраняем данные в базе данных или другом хранилище

            return render(request, 'app/anketa.html', {'form': form, 'data': data})

    else:
        form = AnketaForm()

    return render(request, 'app/anketa.html', {'form': form})



def layout_view(request):
    return render(request, 'app/layout.html', {})

def index(request):
    return render(request, 'app/index.html')
def rooms(request):
    return render(request, 'app/rooms.html')
def add(request):
    return render(request, 'app/add.html')
def contacts(request):
    return render(request, 'app/contacts.html')
def feedback(request):
    return render(request, 'app/feedback.html')

def about(request):
    return render(request, 'app/about.html')
def add(request):
    return render(request, 'app/add.html')
def booking(request):
    return render(request, 'app/booking.html')



def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})  # Возвращаем JSON об успешной отправке
        else:
            # Если форма не валидна, возвращаем ошибки валидации в JSON
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = FeedbackForm()
    return render(request, 'app/feedback.html', {'form': form})