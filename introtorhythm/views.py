from django.shortcuts import render

def index(request):
    return render(request, 'app.html', {
        'title': 'Live',
        'page': 'index'
    })
