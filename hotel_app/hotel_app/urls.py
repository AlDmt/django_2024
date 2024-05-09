"""
URL configuration for hotel_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app import views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('add/', views.add, name='add'),
    path('feedback/', views.feedback, name='feedback'),
    path('contacts/', views.contacts, name='contacts'),
    path('anketa/',views.anketa_view, name='anketa'),
    path('registration/', views.registration, name='registration'),
    path('about/', views.about, name='about'),
    path('registration/', views.registration, name= 'registration'),
    path('booking/', views.booking, name='booking'),
]