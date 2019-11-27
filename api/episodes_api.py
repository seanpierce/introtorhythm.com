import json

from django.http import HttpResponse
from django.views.generic import View

from episodes.repository import EpisodeRepository as repo

class RecentEpisodes(View):
    """
    Returns most recent episode data.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(repo.get_episodes(6)), content_type="application/json")