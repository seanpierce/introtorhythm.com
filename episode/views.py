import json

from django.shortcuts import render

from .repository import EpisodeRepository as repo

def index(request, number=None):
    """Default view for the application.
    
    Args:
        number: An optional argument passed in through the url.

    Returns: 
        Paginated list of number-title episode data.
        If a number argument is supplied, and that matches the number of an episode, 
            a dict containing the matching episide's data will be returned.
            Else, a 404 page will be rendered.
    """

    data = {
        'episodes': repo.get_episode_list(),
        'current_episode': repo.get_current_episode(number)
    }

    if data['current_episode'] is None:
        response = render(request, '404.html')
        response.status_code = 404
        return response

    return render(request, 'index.html', {
        'data': json.dumps(data)
    })
