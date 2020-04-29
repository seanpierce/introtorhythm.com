
import json

from django.shortcuts import render

from content.repository import ContentRepository

def index(request):
    data = {
        'backgroundImage': ContentRepository.get_background_image(),
        'liveCallout': ContentRepository.get_content_by_name('Live Callout'),
    }

    return render(request, 'app.html', {
        'title': 'Live',
        'page': 'index',
        'data': json.dumps(data)
    })

def episodes(request):
    return render(request, 'app.html', {
        'title': 'Episodes',
        'page': 'episodes'
    })

def episode(request, number):
    return render(request, 'app.html', {
        'title': number,
        'page': 'episode',
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