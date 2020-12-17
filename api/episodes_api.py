import json
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from repositories.episodes import EpisodesRepository as repo


class All(View):
    """
    Returns all episode data.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(repo.get_episodes()), content_type="application/json")


@method_decorator(csrf_exempt, name='dispatch')
class Single(View):
    """
    Returns a single episode from the database when provided an episode number.
    """
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        number = body['number']
        return HttpResponse(json.dumps(repo.get_episode(number)))
