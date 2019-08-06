import json

from django.shortcuts import render
from .repository import EpisodeRepository as repo

def index(request):
    data = {
        'episodes': repo.get_episode_list(),
        'current_episode': repo.get_current_episode()
    }
    return render(request, 'index.html', {
        'data': json.dumps(data)
    })
