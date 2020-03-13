from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'app.html', {
        'title': 'Live',
        'page': 'index',
        'config': settings.CHAT_CONFIG
    })

def episodes(request):
    return render(request, 'app.html', {
        'title': 'Episodes',
        'page': 'episodes',
        'config': settings.CHAT_CONFIG
    })

def episode(request, number):
    return render(request, 'app.html', {
        'title': number,
        'page': 'episode',
        'config': settings.CHAT_CONFIG
    })

def unsubscribe(request):
    return render(request, 'app.html', {
        'title': ':(',
        'page': 'unsubscribe'
    })

def archive(request):
    return render(request, 'app.html', {
        'title': 'Archive',
        'page': 'archive'
    })