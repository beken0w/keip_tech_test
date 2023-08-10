# Generated by Django 4.2.4 on 2023-08-10 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('showbuss', 'Шоу-Биз'), ('accidents', 'Происшествия'), ('sport', 'Новости спорта Казахстана'), ('politics', 'Политика'), ('economics', 'Экономика'), ('society', 'Общество'), ('world', 'В мире')], max_length=30, verbose_name='Категория')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 8, 10, 22, 14, 37, 813478), verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок новости')),
                ('text', models.TextField(max_length=5000, verbose_name='Текст новости')),
                ('image', models.ImageField(blank=True, help_text='Выберите директорию изображения', upload_to='img_news/', verbose_name='Картинка')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]