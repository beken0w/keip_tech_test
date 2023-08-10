from datetime import datetime as dt
from django.db import models
from django.urls import reverse


CHOICES = (
    ('showbuss', 'Шоу-Биз'),
    ('accidents', 'Происшествия'),
    ('sport', 'Новости спорта Казахстана'),
    ('politics', 'Политика'),
    ('economics', 'Экономика'),
    ('society', 'Общество'),
    ('world', 'В мире')
)


class News(models.Model):
    category = models.CharField('Категория', choices=CHOICES, max_length=30)
    date = models.DateTimeField('Дата публикации', default=dt.now())
    title = models.CharField('Заголовок новости', max_length=200)
    text = models.TextField('Текст новости', max_length=5000)
    image = models.ImageField(
        'Картинка',
        help_text='Выберите директорию изображения',
        upload_to='media/img/',
        blank=True
    )

    class Meta:
        ordering = ['-id']
