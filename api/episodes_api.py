import json
from django.http import HttpResponse
from django.views.generic import View
from repositories.episodes import EpisodesRepository as repo
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class All(View):
    """
    Returns all episode data.
    """

    def get(self, request, *args, **kwargs):
        data = repo.get_episodes()
        return HttpResponse(json.dumps(data), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class Single(View):
    """
    Returns a single episode from the database when provided an episode number.
    """

    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        data = repo.get_episode(payload['number'])
        return HttpResponse(json.dumps(data), content_type='application/json')
