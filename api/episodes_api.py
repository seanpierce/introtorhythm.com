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


class Single(View):
    """
    Returns a single episode from the database when provided an episode number.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Add decorator to internal class method to
        ignore the presence of a csrf token/ cookie in the request.
        """
        return super(Single, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        number = body['number']
        return HttpResponse(json.dumps(repo.get_episode(number)))
