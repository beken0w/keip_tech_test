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


class Post(models.Model):
    category = models.CharField(choices=CHOICES, max_length=30)
    date = models.DateTimeField(default=dt.now())
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)
    
    def get_absolute_url(self):
        return reverse('news:category',args=[self.category])

