# Generated by Django 5.0.1 on 2024-05-09 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_anketa_gender_anketa_internet'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anketa',
            options={'verbose_name': 'Анкета', 'verbose_name_plural': 'Анкеты'},
        ),
        migrations.RemoveField(
            model_name='anketa',
            name='agree_to_news',
        ),
        migrations.AddField(
            model_name='anketa',
            name='notice',
            field=models.BooleanField(default=False, verbose_name='Получать новости на e-mail?'),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='gender',
            field=models.CharField(choices=[('1', 'Мужской'), ('2', 'Женский')], max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='internet',
            field=models.CharField(choices=[('1', 'Ежедневно'), ('2', 'Раз в несколько дней'), ('3', 'Раз в неделю')], max_length=1, verbose_name='Использование интернета'),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='job',
            field=models.CharField(max_length=100, verbose_name='Род занятий'),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='message',
            field=models.TextField(verbose_name='Коротко о себе'),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]