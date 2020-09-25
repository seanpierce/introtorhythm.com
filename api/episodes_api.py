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
