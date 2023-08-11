from django.shortcuts import render
from news.models import News


def main(request):
    if News.objects.count() >= 10:
        news = News.objects.all()[:10]
        showbuss = News.objects.filter(category='showbuss')
        world = News.objects.filter(category='world')
        context = {
            'news': news,
            'big_main_news': news[0],
            'big_small_news': news[1:3],
            'side_news': news[3:7],
            'circles': news[1:5],
            'horizontal_demo': showbuss,
            'horizontal_plus': world,
            'horizontal_left': world[0],
            'horizontal_right': world[1:4],
            'has_news': True
        }
    else:
        context = {
            'has_news': False
        }
    return render(request, 'includes/news.html', context)


def news_detail(request, news_id=None):
    one_news = News.objects.get(id=news_id)
    context = {
        'one_news': one_news,
    }
    return render(request, 'includes/news_detail.html', context)


def all_news(request):
    list_news = News.objects.all()
    context = {
        'list_news': list_news,
    }
    return render(request, 'includes/list_news.html', context)


def category(request, category=None):
    list_news = News.objects.filter(category=category)
    context = {
        'list_news': list_news,
    }
    return render(request, 'includes/list_news.html', context)


def info(request, type='about'):
    if type.lower() == 'about':
        text = "Здесь информация о Нас"
    elif type.lower() == 'price':
        text = "Здесь информация о Рекламе"
    elif type.lower() == 'rule':
        text = "Здесь информация о Правилах"
    elif type.lower() == 'conf':
        text = "Здесь информация о Политике Конфиденциальности"
    else:
        text = "Такой страницы нет"
    context = {
        'text': text
    }
    return render(request, "includes/info.html", context)
