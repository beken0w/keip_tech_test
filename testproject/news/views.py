from django.shortcuts import render
from news.models import Post


def main(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'includes/posts.html', context)


def category(request, category=None):
    posts = Post.objects.filter(category=category)
    context = {
        'posts': posts,
    }
    return render(request, 'includes/posts.html', context)
