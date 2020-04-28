
import json

from django.shortcuts import render

from content.repository import ContentRepository

def index(request):
    mvcData = {
        'page': 'index',
        'backgroundImage': ContentRepository.get_background_image(),
        'liveCallout': ContentRepository.get_content_by_name('Live Callout'),
    }

    return render(request, 'app.html', {
        'title': 'Live',
        'mvcData': json.dumps(mvcData)
    })

def episodes(request):
    mvcData = {
        'page': 'episodes',
    }

    return render(request, 'app.html', {
        'title': 'Episodes',
        'mvcData': json.dumps(mvcData)
    })

def episode(request, number):
    mvcData = {
        'page': 'episode',
    }

    return render(request, 'app.html', {
        'title': number,
        'mvcData': json.dumps(mvcData)
    })

def unsubscribe(request):
    mvcData = {
        'page': 'unsubscribe'
    }

    return render(request, 'app.html', {
        'title': ':(',
        'mvcData': json.dumps(mvcData)
    })

def archive(request):
    mvcData = {
        'page': 'archive'
    }

    return render(request, 'app.html', {
        'title': 'Archive',
        'mvcData': json.dumps(mvcData)
    })