import json

from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from episodes.repository import EpisodeRepository as repo

class Recent(View):
    """
    Returns most recent episode data.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(repo.get_episodes(6)), content_type="application/json")

class All(View):
    """
    Returns all episode data.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(repo.get_episodes()), content_type="application/json")


class Search(View):
    """
    Searches for Episode objects where input is contained in an Episode's content.
    """
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        """
        Add decorator to internal class method to
        ignore the presence of a csrf token/ cookie in the request.
        """
        return super(Search, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        search_text = body['search']
        return HttpResponse(json.dumps(repo.search(search_text)), content_type="application/json")

class Episode(View):
    """
    Returns episode data when provided an episode number.
    """

    def get(self, request, *args, **kwargs):
        number = self.kwargs['number']
        return HttpResponse(json.dumps(repo.get_episode_by_number(number)), content_type="application/json")