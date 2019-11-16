import json

from django.shortcuts import render

from .repository import EpisodeRepository as repo

def index(request):
    """Default view for the application.

    Returns:
        Paginated list of number-title episode data.
        A dict containing data from the most recent episode.
    """

    current_episode = repo.get_current_episode()

    return render(request, 'app.html', {
        'data': json.dumps(current_episode),
        'number': current_episode['number'],
        'title': current_episode['number'] + '- ' + current_episode['title'],
        'neighbors': json.dumps(repo.get_neighbor_episode_numbers(current_episode['number']))
    })

def episode(request, number):
    """A specific episode view

    Args:
        A number, supplied via the url in the request.

    Returns:
        If an episode is found, given the specified episode number,
        the method will return a paginated list of number-title episode data beginning
        at the specified episode and ending with the 10th most recent episode after.
        A dict containing data from the specified episode.

        If the specified episode was not found, the method will return a 404 error page.
    """

    current_episode = repo.get_current_episode(number)

    if current_episode is None:
        response = render(request, '404.html')
        response.status_code = 404
        return response

    return render(request, 'app.html', {
        'data': json.dumps(current_episode),
        'title': current_episode['number'] + '- ' + current_episode['title'],
        'neighbors': json.dumps(repo.get_neighbor_episode_numbers(current_episode['number']))
    })


def archive(request):
    """Archive view for SEO purposes

    Returns:
        A list of all active episode numbers and titles in descending order.
    """

    data = {
        'episodes': repo.get_all_episode_list()
    }

    return render(request, 'app.html', {
        'data': json.dumps(data),
        'title': 'Archive'
    })

def live(request):
    return render(request, 'live.html', {
        'title': 'Live'
    })
