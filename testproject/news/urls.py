from django.urls import path
from news.views import main, category

app_name = 'news'

urlpatterns = [
    path('', main, name='main'),
    path('<str:category>/', category, name='category'),
]
