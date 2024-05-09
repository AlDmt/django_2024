import datetime
from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render,redirect

from .forms import  FeedbackForm
from .forms import  AnketaForm
from django.contrib.auth.forms import UserCreationForm

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


