# hotel_app/models.py

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    agree_to_news = models.BooleanField(default=False)  # Новое поле для согласия на получение новостей

    def __str__(self):
        return self.name


class Anketa(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    job = models.CharField(max_length=200)
    GENDER_CHOICES = [
        ('M', 'мужской'),
        ('F', 'женский'),
        ('unknown', 'unknown'),
    ]
    INTERNET_CHOICES = [
        ('daily', 'daily'),
        ('every_two_days', 'every_two_days'),
        ('weekly', 'weekly'),
        ('unknown', 'неизвестно'),
    ]
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default="unknown")
    internet = models.CharField(max_length=20, choices=INTERNET_CHOICES, default="unknown")
    email = models.EmailField()
    message = models.TextField()
    agree_to_news = models.BooleanField(default=False)  