import json

from django.shortcuts import render

from .repository import EpisodeRepository as repo

# Create your views here.
def index(request):
    episodes = repo.getEpisodeList()
    return render(request, 'index.html', {
        'episodes': json.dumps(list(episodes))
    })
