from django.urls import path
from news.views import main, category, news_detail, all_news, info

app_name = 'news'

urlpatterns = [
    path('', main, name='main'),
    path('all/', all_news, name='all_news'),
    path('info/<str:type>/', info, name='info'),
    path('news/<int:news_id>/', news_detail, name='news_detail'),
    path('category/<str:category>/', category, name='category')
]
