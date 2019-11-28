from django.shortcuts import render

def index(request):
    return render(request, 'app.html', {
        'title': 'Live',
        'page': 'index'
    })

def episodes(request):
    return render(request, 'app.html', {
        'title': 'Episodes',
        'page': 'episodes'
    })
