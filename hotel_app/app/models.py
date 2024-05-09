# hotel_app/models.py

from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    agree_to_news = models.BooleanField(default=False)  # Новое поле для согласия на получение новостей

    def __str__(self):
        return self.name


from django.db import models

class Anketa(models.Model):
    second_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    RESERVATION_CHOICES = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    )

    reservation = models.CharField(
        verbose_name='Насколько быстро и просто вы забронировали номер?',
        choices=RESERVATION_CHOICES,
        max_length=1,
        default='5'  # Установка значения по умолчанию на '5'
    )
    city = models.CharField(max_length=100, verbose_name='Ваш город')
    job = models.CharField(max_length=100, verbose_name='Ваш род занятий')
    work = models.CharField(
        max_length=1,
        choices=(('5','5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')),
        default='5',
        verbose_name='Оцените качество работы персонала'
    )
    back = models.CharField(max_length=1, choices=(('1','Да'), ('2', 'Нет')), verbose_name='Хотели бы вы приехать к нам еще?')
    email = models.EmailField(verbose_name='Ваш e-mail')
    message = models.TextField(verbose_name='Отзыв')
    notice = models.BooleanField(default=False, verbose_name='Хочу получать новости на электронную почту')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'
